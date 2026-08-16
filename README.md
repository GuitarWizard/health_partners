# Hospital Data ETL Pipeline

Automated pipeline to fetch, process, and standardize hospital datasets from the CMS Provider Data catalog.

## Overview
This project automates the discovery and downloading of hospital-related CSV datasets from the CMS metastore. It includes:
- **Incremental Updates**: Only processes datasets that have been updated since the previous job execution
- **Data Standardization**: Converts dataset headers to `snake_case` for consistent field labeling.
- **Concurrent Processing**: Downloads and processes multiple datasets in parallel to optimize execution time.
- **Automation**: yaml file structured to run daily at 2 am.

## Features
- Fetches the full CMS dataset catalog via API.
- Filters for datasets related to "Hospitals".
- Maintains a local `cms_download_metadata.json` state file to track modifications.
- Standardizes column headers (e.g., "Patients’ rating" → `patients_rating`).

## Requirements
- `pandas`
- `requests`

## How it works
1. **Catalog Fetching**: Retrieves the list of all datasets from the CMS API.
2. **Filtering**: Identifies datasets tagged with "Hospitals".
3. **State Tracking**: Compares the API's `modified` timestamp with the local `cms_download_metadata.json` file.
4. **Execution**: Downloads and processes only new or modified datasets using a `ThreadPoolExecutor`.
5. **Metadata Update**: Saves the results to `cms_download_metadata.json` and optionally commits the update to the repository.

## Automation
The pipeline is configured to run daily at 2:00 AM UTC. It handles:
- Environment setup (Python 3.11).
- Dependency management (pip).
- Execution of the ETL script.
- Automatic committing of the updated metadata file back to the repository.
