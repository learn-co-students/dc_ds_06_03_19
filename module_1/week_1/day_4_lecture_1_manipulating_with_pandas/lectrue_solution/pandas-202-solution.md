### Manipulating Data With Pandas 
#### Relevant solution code

Import pandas

```
import pandas as pd
```


Read the dataset into memory from a url

```
animal_outcomes = pd.read_csv('https://data.austintexas.gov/api/views/9t4d-g238/rows.csv?accessType=DOWNLOAD')
```

Get value counts

```
animal_outcomes.breed.value_counts()[:5]
animal_outcomes.loc[(animal_outcomes['animal']=='Dog') & (animal_outcomes['outcome']=='Adoption')].breed.value_counts()
```


Check the column names of the dataset and rename them.

```
animal_outcomes.columns
new_names = ['id', 'name', 'date', 'monthyear', 'dob', 'outcome', 'outcome_s', 'animal', 'sex', 'age', 'breed', 'color']

animal_outcomes.columns = new_names
```

Check data types of columns

```
animal_outcomes.dtypes
```


Fix the age variable

```
# drop the original age variable
animal_outcomes.drop(columns = ['age'], inplace = True)

# grab the first 10 digits of the date
animal_outcomes['date']=animal_outcomes['date'].map(lambda x: x[:10])

# convert the string 'date' to a datetime object using pd.to_datetime()
animal_outcomes['date'] =  pd.to_datetime(animal_outcomes['date'], format='%m/%d/%Y', errors = 'ignore')

# do the same to date of birth
animal_outcomes['dob'] =  pd.to_datetime(animal_outcomes['dob'], format='%m/%d/%Y', errors = 'ignore')

# calculate the difference between date of outcome and date of birth
animal_outcomes['age_in_days'] = (animal_outcomes['date'] - animal_outcomes['dob'])

# convert the age_in_days to years by dividing the days by 365
animal_outcomes['years'] = animal_outcomes['age_in_days'].map(lambda x: x.days/365)
```

Get some groupby info
```
animal_outcomes.groupby('animal').mean()
animal_outcomes.groupby(['animal', 'sex']).mean()

```
