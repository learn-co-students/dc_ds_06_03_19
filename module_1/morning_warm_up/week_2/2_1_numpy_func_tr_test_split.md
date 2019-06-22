# [HARD] warm-up

### Import packages
`import pandas as pd`

`import numpy as np`

### Create a function to split data into training data and testing data
##### When applying machine learning algorithms in a supervised learning scenario we want to have data to learn from and some data we have never seen before to test what we have learnt. 

### We have two tasks: 
- 	Choosing a condition to split the data on (e.g. we 	gonna choose the year 2010)
-  Split the features from the target we want to 	predict

### 1. Open your CO2 notebook (from yesterday) through terminal!
`use commands cd and jupyter notebook`

### 2. If not done yesterday, pick the year column, month column, day column and C02 column from the dataframe

### 3. Create the function
 - cond_df is an array of the column you want to condition your split on
 - the idea is to use np.where on the condition column to get the indices on which the full dataset will be split
 - once we have the indices we can use them on the full dataset to make the split. Notice: the indices of the conditioned column and the pandas df are one and the same.
 - X are all the features and Y should be the CO2 column - please split them before executing the function and assign them to X annd Y 
 
`def tr_te_split(X, Y, cond_df, cond):`

`cond_df could be an array of the year column`
							
`use np.where
`

### 4. Check the data sets to see if your split worked (can do manually - with your eyes)


### 5. git push it to your branch!


### [optional] 6. Explore the use of the describe(), info() and dtypes on the pandas df before turnnnig it to numpy array 
