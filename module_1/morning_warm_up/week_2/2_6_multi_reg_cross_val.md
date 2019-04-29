### Import packages
`import numpy as np`

### 1. same as yesterday we are going to create a function for fake noraml distribution however this time we want our X to be high dimensional 
`use np.random.multivariate_normal`

### 2. Create at the same way the equations y = xw + noise  
pay attention that this time we will need high dimensional w.
`use np.matmul`

-  think before you write, which dimension should the noise be ? 


### 2.5 [optional] Can you plot some of it in 3-d ? 

### 3. [*HARD] We now want to write two functions:
 - one for splitting indices randomly 
 - input those to a cross validation function
 
#####-- can your function deal with 7/8/21-fold cross validation ? 

#### hints : 
 `use numpy random permutation`
 `def rand_idx_split(tr_abs, te_abs, val_abs)`
 `def cv_split(k, iter_num, x, y, tr_val_idx)`
     
     '''# k - number of folds
    # iter - iteration number
    # x - training set
    # y- trianing targets
    # tr_val_idx - all indices of columns coressponding to training or validation
    # RETURNS: new train and validation sets''' 
 
- remember to sort the indices after permutation 


### 4. push everything to github 

### 5. [optional] : 
### 5.1. first split data to training and testing - write a funtion !
### 5.2. split the dataset from above using SKlearn cross-validation 
`from sklearn import datasets, linear_model`
`from sklearn.model_selection import cross_val_score`
`use cross-val score` 


### 6. [optional] : 
### 6.1. Download sublime text and pep8 formatting package 
### 6.2. Download all your notebook as .py and open the .py scripts with sublime 
### 6.3. put your .py scripts as-is in your repository - using command line mv
### 6.4. now, go to the .py files and use pep8 to re-format the code to best practice 
### 6.5. push the new version to your branch 
### 6.6. have a look at the history of the .py scripts in your repository to see the difference between your tendencies to best practice coding norms. 

