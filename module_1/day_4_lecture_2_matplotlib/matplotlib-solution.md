### Intro to Matplotlib
#### Relevant solution code


#### Bar Charts

```
# Get data for Dog bar chart
dog_month=animal_shelter_df[(animal_shelter_df['animal']=='Dog') & (animal_shelter_df['year']==2018) ].groupby('i_month').size()

# Make chart
ax = plt.subplot() 
months = dog_month.index 

plt.bar(months, dog_month, color = 'green')

ax.set_xticks(months) # set ticks values, as a method of the axes
ax.set_xticklabels(months) # set tick labels, also as a method of the axes

plt.title('Intake of Dogs per month in 2018')
plt.xlabel('months')
plt.ylabel('intake count')
plt.show()

# Get data for Cat bar chart
cat_month = animal_shelter_df[(animal_shelter_df['animal']=='Cat') & (animal_shelter_df['year']==2018) ].groupby('i_month').size()

# Make plot
ax = plt.subplot() 
months = cat_month.index 

plt.bar(months, cat_month, color = 'green')

ax.set_xticks(months) # set ticks values, as a method of the axes
ax.set_xticklabels(months) # set tick labels, also as a method of the axes

plt.title('Intake of cats per month in 2018')
plt.xlabel('months')
plt.ylabel('intake count')
plt.show()


```


we can create overlaid or side-by-side bargraph. You need to shift the x value by width to accommodate for two graphs.
Adjust the code below to be in line with the new variables we defined above

```
from matplotlib import pyplot as plt

fig = plt.figure()
n = 1 # This is our first dataset (out of 2) 
t = 1 # Number of datasets 
d = 12 # Number of sets of bars 
w = 0.4 # Width of each bar 
dog_values = [t*element + w*n for element in range(d)] 
# essentially, this list comprehension gives us the position of the position of dogs

plt.bar(dog_values,dog_num, color='blue')
n = 2  # This is our second dataset (out of 2)
t = 1 # Number of datasets
d = 12 # Number of sets of bars
w = 0.4 # Width of each bar
cat_values = [t*element + w*n for element in range(d)]

plt.bar(cat_values, cat_num, color = 'purple')
ax.set_xticks(range(0,len(dog_month))) # set ticks values, as a method of the axes
ax.set_xticklabels(dog_month) # set tick labels, also as a method of the axes
plt.legend(["dogs", "cats"])
plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'))
n = 1
```


#### Histograms

```
# Get cat data
cats =animal_shelter_df[(animal_shelter_df['animal']=='Cat') & (animal_shelter_df['year']==2018) ].years_old

# Get dog data
dogs =animal_shelter_df[(animal_shelter_df['animal']=='Dog') & (animal_shelter_df['year']==2018) ].years_old

# Make plot
plt.figure(figsize = (10,8))
plt.hist(cats, bins = 20, alpha = .35, color = "blue", density = True,) # <- alpha is transparency 
plt.hist(dogs, bins = 20, alpha = .35, color = "green",density = True,)


plt.legend(["cats", "dogs"])

plt.xlabel('age at outcome')
plt.ylabel('Frequency of Values')
plt.title('distribution of age at outtake: cats vs dogs')
```


#### Scatter Plots

```
# Get dog data
dogs_age =animal_shelter_df[(animal_shelter_df['animal']=='Dog') & (animal_shelter_df['year']==2018) & (animal_shelter_df['outcome']=="Adoption") ].years_old

dogs_time = animal_shelter_df[(animal_shelter_df['animal']=='Dog') & (animal_shelter_df['year']==2018) & (animal_shelter_df['outcome']=="Adoption") ].days_in_shelter

# make plot
plt.scatter(dogs_age, dogs_time )
plt.title('Scatter Plot of Time spent in shelter compared to age')
plt.legend()

```

#### Pie charts

```
# Pie charts take a groupby series
cats =animal_shelter_df[(animal_shelter_df['animal']=='Cat') & (animal_shelter_df['year']==2018) ].groupby('outcome').size()

# Make plot
plt.figure(figsize=(10,8))
plt.pie(cats, labels = cats.index, autopct="%1d%%")

plt.axis('equal')
plt.title('outcomes')
plt.savefig("catoutcomes.jpeg")
plt.show()
```