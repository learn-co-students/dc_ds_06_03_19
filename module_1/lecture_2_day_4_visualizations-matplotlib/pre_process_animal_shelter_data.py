import pandas as pd

def transform_string_to_date(pd_series):
    pd_series = pd.to_datetime(pd_series).dt.date
    return pd_series

def rename_col_df(old_col, new_col, df):
    df = df.rename(columns={old_col: new_col})
    return df

def remove_miss_col_with_bigger_than_share(df, share):
    df = df.loc[:, (df.isnull().sum(axis=0) / df.shape[0]) <= share]
    
    return df


def pre_process_animal_shelter():
    ### Read datasets 
    intake = pd.read_csv('./Austin_Animal_Center_Intakes.csv')
    animal_outcomes = pd.read_csv('https://data.austintexas.gov/api/views/9t4d-g238/rows.csv?accessType=DOWNLOAD')
    ### drop extranous columns
    intake = intake.drop(['MonthYear', 'Name', 'Breed', 'Color', 'Sex upon Intake'] , axis=1)
    animal_outcomes = animal_outcomes.drop('MonthYear', axis=1)
    
    ## change date column from string to date and add year, month and day columns (Can you think how to write this section with shorter code ?)
    intake['DateTime'], animal_outcomes['DateTime']  = list( map(transform_string_to_date, \
                                                                 [intake['DateTime'], animal_outcomes['DateTime']]))
    intake['year'], animal_outcomes['year'] = intake['DateTime'].apply( lambda x: x.year), \
                                                                animal_outcomes['DateTime'].apply( lambda x: x.year)

    intake['month'], animal_outcomes['month'] = intake['DateTime'].apply( lambda x: x.month), \
                                                                animal_outcomes['DateTime'].apply( lambda x: x.month)

    intake['day'], animal_outcomes['day'] = intake['DateTime'].apply( lambda x: x.day), \
                                                                animal_outcomes['DateTime'].apply( lambda x: x.day)
    ## make sure Animal ID columns are of type string and rename column
    intake['Animal ID'], animal_outcomes['Animal ID']  = intake['Animal ID'].astype(str), \
                                                            animal_outcomes['Animal ID'].astype(str) 
    intake, animal_outcomes = rename_col_df('Animal ID', 'animal_id', intake), \
                                                            rename_col_df('Animal ID', 'animal_id', animal_outcomes)
    ### merge datasets
    animal_shelter_df  = pd.merge(intake, animal_outcomes, on=['animal_id', 'year'], \
                                  how='left', suffixes=('_intake', '_outcome'))
    
    ### Clean 
    ### 1. columns with too many missing values 
    ### 2. rows with no outcome or with wrong outcome date (i.e. smaller than intake)
    animal_shelter_df = remove_miss_col_with_bigger_than_share(animal_shelter_df, 0.5)
    animal_shelter_df = animal_shelter_df[(~animal_shelter_df['DateTime_outcome'].isna()) & \
                                          (animal_shelter_df['DateTime_outcome'] > animal_shelter_df['DateTime_intake'])]
    
    ### Add days in shelter column
    animal_shelter_df['days_in_shelter'] = (animal_shelter_df['DateTime_outcome'] - animal_shelter_df['DateTime_intake'])

    animal_shelter_df['days_in_shelter'] = animal_shelter_df['days_in_shelter'].apply(lambda x: x.days)
                                                              
    
    return animal_shelter_df.reset_index(drop=True)

