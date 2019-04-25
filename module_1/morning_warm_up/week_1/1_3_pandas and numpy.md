# Pandas and numpy - pair-up
### Discussion session

1. How will you read the following data into a pandas data frame ? 
 ` ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt`
 
2. How would you pick columns 0,1,3 ?  
`[[0, 1, 3]]`

3. Use a for loop to find all rows where 
Co2 (column 3) enteries with the value -99.99 (these are missing values) and replace them with NaN values (try using np.nan - do you know what it is? )

4. Change names of columns to year, month, and CO2 (use colnames)

5. Add a column 'Day' and specifiy the day 15 for all enteries

6. Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it)) 

7. Drop the 'Day' column

8. use pandas groupby to print the yeaerly avg. of co2 per year. 

9. Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)

10. repeat step (3) but this time using the np.where command. 

11. Download the notebook as .py script and run it from your terminal. 

12. Create a branch in github repository called warm_up_draft   

13. push the notebook with the name CO2 to your new branch on github.
