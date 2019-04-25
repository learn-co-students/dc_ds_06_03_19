#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import pandas as pd

# Read in shelter data
animal_outcomes=pd.read_csv('https://data.austintexas.gov/api/views/9t4d-g238/rows.csv?accessType=DOWNLOAD') 

# change names
new_names = ['id', 'name', 'date', 'monthyear', 'dob', 'outcome', 'outcome_s', 'animal', 'sex', 'age', 'breed', 'color']
animal_outcomes.columns = new_names

# convert date formats
animal_outcomes.date = animal_outcomes['date'].map(lambda x: x[:10])
animal_outcomes['o_date'] =  pd.to_datetime(animal_outcomes['date'], format='%m/%d/%Y')
animal_outcomes['dob'] =  pd.to_datetime(animal_outcomes['dob'], format='%m/%d/%Y')

# get more date info
animal_outcomes['o_month'] = animal_outcomes['o_date'].map(lambda x: x.month)
animal_outcomes['year'] = animal_outcomes['o_date'].map(lambda x: x.year)
animal_outcomes['o_weekday'] = animal_outcomes['o_date'].map(lambda x: x.weekday())

#get age of animal
# I do not know why I had to cast them again... but it only worked when i did
animal_outcomes['date'] =pd.to_datetime(animal_outcomes['date'])
animal_outcomes['dob'] =pd.to_datetime(animal_outcomes['dob'])
animal_outcomes['age_in_days'] = animal_outcomes['date'] - animal_outcomes['dob']

animal_outcomes['years_old'] = animal_outcomes.age_in_days.map(lambda x: x.days/365)

# drop "unknown" gender
animal_outcomes = animal_outcomes[animal_outcomes.sex != 'Unknown']

# get sex variablle split
animal_outcomes['gender']= animal_outcomes['sex'].str.split(" ").str[1] 
animal_outcomes['o_altered']= animal_outcomes['sex'].str.split(" ").str[0] 

outcomes_data = animal_outcomes[['id', 'name','outcome', 'outcome_s', 'animal','breed', 'o_date', 'years_old', 'o_month', 'year', 'o_weekday', 'o_altered']]

outcomes_data.head()

