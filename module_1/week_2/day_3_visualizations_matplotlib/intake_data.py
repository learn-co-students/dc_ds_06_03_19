#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import pandas

import pandas as pd

# read in some data
intakes = pd.read_csv('https://data.austintexas.gov/api/views/wter-evkm/rows.csv?accessType=DOWNLOAD')

# rename columns
new_names = ['id', 'name', 'i_date', 'monthyear', 'found_loc', 'intake_type', 'intake_con', 'type', 'sex', 'age', 'breed', 'color']
intakes.columns = new_names

# drop NaNs 
intakes.dropna(inplace=True)

# keep only a few columns
intake_data = intakes[['id','type', 'i_date', 'sex']]

# Clean code
intake_data['i_date']=intake_data['i_date'].map(lambda x: x[:10])
intake_data['i_date'] =  pd.to_datetime(intake_data['i_date'], format='%m/%d/%Y', errors = 'ignore')

# get more date info
intake_data['i_month'] = intake_data['i_date'].map(lambda x: x.month)
intake_data['year'] = intake_data['i_date'].map(lambda x: x.year)
intake_data['i_weekday'] = intake_data['i_date'].map(lambda x: x.weekday())

# drop "unknown" gender
intake_data = intake_data[intake_data.sex != 'Unknown']

# get sex variablle split
intake_data['gender']= intake_data['sex'].str.split(" ").str[1] 
intake_data['i_altered']= intake_data['sex'].str.split(" ").str[0] 

