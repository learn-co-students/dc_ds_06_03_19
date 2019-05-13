### import 
``` 
	import statsmodels
	import numpy as np
	import matplotlib.pylab as plt
```

### 1. create a matrix (numpy array) of ones sized (100 X 50) 

`use .shape to check your matrix`

### 2. create a matrix of zeros the same size as the matrix from (1)
`use numpy`

### 3. create a new matrix that will be the concatenation of (1 & 2) --> matrix sized (200, 50)

### 4. Add the two matrices (from 1 & 2) to get one matrix (100 X 50) --> check yourself (do all enteries show 1?)

### 5. Use the function we have created few warm-ups ago to create two matrices 20X40 from multivariate normal distribution

### 6. let's try to make two operations: 
    # - matrix multiplication (first test it on a 2X2 matrices)
    # - element wise multiplication 
### 7. let's create again the linear equations Y = XW + noise
##### Noise should come from univariate normal distribution with mean 0 and variance 0.1 


### 8. Can you calculate the weight (coeficients) matrix? Do it.
### Write down the equation of the multiple regression model


### 9. Create a function that calculates the mean squared error 

### 10. Plot the errors to check for normality

### 11. Plot scatter plots of the independent variables against the target value to check for violations of the constant variance assumption for errors 

### 12. Calculate R squared (you can use statsmodels)