#!/usr/bin/env python
# coding: utf-8

# In[ ]:


animal_shelter_df  = pd.merge(intake_data, outcomes_data, on=['id', 'year'],                                   how='left', suffixes=('_intake', '_outcome'))

animal_shelter_df = animal_shelter_df[(~animal_shelter_df['o_date'].isna()) &                                           (animal_shelter_df['o_date'] > animal_shelter_df['i_date'])]

animal_shelter_df['days_in_shelter'] = (animal_shelter_df['o_date'] - animal_shelter_df['i_date'])

animal_shelter_df['days_in_shelter'] = animal_shelter_df['days_in_shelter'].apply(lambda x: x.days)
                                                              

