#!/usr/bin/env python
# coding: utf-8

# This is an exploratory script, not for "production" purposes

# In[10]:


# import pandas as pd
import requests
import re
import pprint


# In[11]:


printer = pprint.PrettyPrinter(indent=4, width=50, sort_dicts=True)


# In[12]:


CMS_METASTORE_URL = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items"
STATE_FILE = "cms_download_metadata.json"
OUTPUT_DIR = "./hospital_datasets"


# Get a clean visual of the json structure, a preview of the .csv files beforehand

# In[14]:


response = requests.get(CMS_METASTORE_URL, timeout=30)
response.raise_for_status()
all_datasets = response.json()
printer.pprint(all_datasets[0])


# Notes:
# 
# * there's a unique identifier tag
# * a csv downlload url uner distribution.donaloadURL
# * a modified field recording date of change
# 

# In[ ]:




