#!/usr/bin/env python
# coding: utf-8

# In[3]:


import concurrent.futures
import json
import logging
import os
import re
from datetime import datetime, timezone
import pandas as pd
import requests


# In[4]:




# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

CMS_METASTORE_URL = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items"
STATE_FILE = "cms_download_metadata.json"
OUTPUT_DIR = "./hospital_datasets"


def to_snake_case(header: str) -> str:
    """
    Converts mixed-case string with spaces/special characters to clean snake_case.
    Example: "Patients’ rating of the facility linear mean score" -> 
             "patients_rating_of_the_facility_linear_mean_score"
    """
    # Remove apostrophes/quotes without adding spaces (e.g., Patients' -> Patients)
    header = re.sub(r"['’`‘]", "", header)
    # Replace non-alphanumeric characters with spaces
    header = re.sub(r"[^\w\s]", " ", header)
    # Strip leading/trailing whitespace, lowercase, and join on single underscore
    header = header.strip().lower()
    return re.sub(r"\s+", "_", header)


def load_metadata_state(filepath: str) -> dict:
    """Loads state tracking dictionary from local JSON file."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return {}


def save_metadata_state(filepath: str, state: dict) -> None:
    """Saves updated state tracking dictionary to local JSON file."""
    with open(filepath, "w") as f:
        json.dump(state, f, indent=2)


def fetch_hospital_datasets() -> list:
    """Fetches full metastore catalog from CMS and filters for 'Hospitals' theme."""
    logging.info("Fetching metastore catalog from CMS API...")
    response = requests.get(CMS_METASTORE_URL, timeout=30)
    response.raise_for_status()
    all_datasets = response.json()
    

    hospital_datasets = []
    for dataset in all_datasets:
        themes = dataset.get("theme", [])
        if isinstance(themes, str):
            themes = [themes]

        # Check if 'Hospitals' exists in dataset themes
        if any("hospital" in theme.lower() for theme in themes):
            hospital_datasets.append(dataset)

    logging.info(f"Found {len(hospital_datasets)} datasets under 'Hospitals' theme.")
    return hospital_datasets


def process_dataset(dataset: dict, output_dir: str) -> tuple[str, dict] | None:
    """
    Downloads CSV distribution, standardizes column headers to snake_case,
    and writes clean csv to output directory.
    """
    ds_id = dataset.get("identifier")
    title = dataset.get("title", ds_id)
    modified_dt = dataset.get("modified", "")

    # Locate CSV download URL from distribution array
    download_url = None
    for dist in dataset.get("distribution", []):
        media_type = dist.get("mediaType", "").lower()
        fmt = dist.get("format", "").lower()
        if "csv" in media_type or fmt == "csv":
            download_url = dist.get("downloadURL")
            break

    if not download_url:
        logging.warning(f"No CSV distribution found for dataset: {title}")
        return None

    logging.info(f"Downloading: {title}")

    try:
        # Read dataset into pandas DataFrame directly from stream
        df = pd.read_csv(download_url, low_memory=False)

        # Transform column headers to snake_case
        df.columns = [to_snake_case(col) for col in df.columns]

        # Generate clean local filename
        file_slug = to_snake_case(title)
        out_filepath = os.path.join(output_dir, f"{file_slug}.csv")

        # Save processed CSV
        df.to_csv(out_filepath, index=False)
        logging.info(f"Successfully processed and saved: {out_filepath}")

        metadata_entry = {
            "title": title,
            "modified": modified_dt,
            "last_processed_at": datetime.now(timezone.utc).isoformat(),
            "local_path": out_filepath
        }
        return ds_id, metadata_entry

    except Exception as e:
        logging.error(f"Failed processing dataset '{title}' ({download_url}): {e}")
        return None


def run_pipeline(max_workers: int = 5):
    """Executes incremental ETL pipeline in parallel."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    state = load_metadata_state(STATE_FILE)
    
    # get the data
    datasets = fetch_hospital_datasets()
    datasets_to_process = []

    # Filter out files that haven't been modified since last run
    for ds in datasets:
        ds_id = ds.get("identifier")
        api_modified = ds.get("modified", "")
        last_modified = state.get(ds_id, {}).get("modified")

        if not last_modified or api_modified > last_modified:
            datasets_to_process.append(ds)
    
    # if all data is current at the job's execution
    if not datasets_to_process:
        logging.info("All Hospital datasets are up-to-date. No downloads needed.")
        return

    logging.info(f"Processing {len(datasets_to_process)} updated/new datasets across {max_workers} worker threads.")

    # Process downloads and transformations concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_dataset, ds, OUTPUT_DIR): ds 
            for ds in datasets_to_process
        }

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                ds_id, meta = result
                state[ds_id] = meta

    # Save updated execution metadata
    save_metadata_state(STATE_FILE, state)
    logging.info("Pipeline execution completed and metadata state saved.")


if __name__ == "__main__":
    run_pipeline(max_workers=5)

