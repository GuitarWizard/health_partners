{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4eee1107-e889-436a-855c-2caa5e838e2c",
   "metadata": {},
   "source": [
    "This is an exploratory script, not for \"production\" purposes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bd19fd27-0c8e-46f0-98c9-b8f5bc940dad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import pandas as pd\n",
    "import requests\n",
    "import re\n",
    "import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b5aa145a-f8b3-453d-a105-4c454012609c",
   "metadata": {},
   "outputs": [],
   "source": [
    "printer = pprint.PrettyPrinter(indent=4, width=50, sort_dicts=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0d225f16-f9b9-4d8e-8769-72028c98d75b",
   "metadata": {},
   "outputs": [],
   "source": [
    "CMS_METASTORE_URL = \"https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items\"\n",
    "STATE_FILE = \"cms_download_metadata.json\"\n",
    "OUTPUT_DIR = \"./hospital_datasets\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b085c48c-89d5-460b-b16e-972abd1ec312",
   "metadata": {},
   "source": [
    "Get a clean visual of the json structure, a preview of the .csv files beforehand"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bdb6c221-8e93-408f-a9bf-8e741e920d5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{   '@type': 'dcat:Dataset',\n",
      "    'accessLevel': 'public',\n",
      "    'bureauCode': ['009:38'],\n",
      "    'contactPoint': {   '@type': 'vcard:Contact',\n",
      "                        'fn': 'Dialysis Facility '\n",
      "                              'Helpdesk',\n",
      "                        'hasEmail': 'mailto:DialysisData@umich.edu'},\n",
      "    'description': 'A list of all dialysis '\n",
      "                   'facilities registered with '\n",
      "                   'Medicare that includes '\n",
      "                   'addresses and phone numbers, '\n",
      "                   'as well as services and '\n",
      "                   'quality of care provided.',\n",
      "    'distribution': [   {   '@type': 'dcat:Distribution',\n",
      "                            'describedBy': 'https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/dialysis/DF_Data_Dictionary.pdf',\n",
      "                            'describedByType': 'application/pdf',\n",
      "                            'downloadURL': 'https://data.cms.gov/provider-data/sites/default/files/resources/c04d84bc5c641284494bee4f20f17f9c_1781625941/DFC_FACILITY.csv',\n",
      "                            'mediaType': 'text/csv'}],\n",
      "    'identifier': '23ew-n7w9',\n",
      "    'issued': '2020-03-14',\n",
      "    'keyword': ['Quality', 'Quality Measures'],\n",
      "    'landingPage': 'https://data.cms.gov/provider-data/dataset/23ew-n7w9',\n",
      "    'modified': '2026-06-16',\n",
      "    'nextUpdateDate': '2026-10-28',\n",
      "    'programCode': ['009:000'],\n",
      "    'publisher': {   '@type': 'org:Organization',\n",
      "                     'name': 'Centers for '\n",
      "                             'Medicare & '\n",
      "                             'Medicaid Services '\n",
      "                             '(CMS)'},\n",
      "    'released': '2026-07-15',\n",
      "    'theme': ['Dialysis facilities'],\n",
      "    'title': 'Dialysis Facility - Listing by '\n",
      "             'Facility'}\n"
     ]
    }
   ],
   "source": [
    "response = requests.get(CMS_METASTORE_URL, timeout=30)\n",
    "response.raise_for_status()\n",
    "all_datasets = response.json()\n",
    "printer.pprint(all_datasets[0])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "288d78c4-6ef2-40d4-9bfe-f54551cb6e8a",
   "metadata": {},
   "source": [
    "Notes:\n",
    "\n",
    "* there's a unique identifier tag\n",
    "* a csv downlload url uner distribution.donaloadURL\n",
    "* a modified field recording date of change\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4e051d0-502a-4313-b71a-93a19d477e63",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
