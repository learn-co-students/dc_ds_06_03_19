---
title: NumPyandPandas
layout: post
weight: 10
hidden: true
---
​
Introducing Libraries: NumPy and Pandas Lesson Plan
===
​
​
**Course**: Data Science   <br/>
**Mod**: Module 1                    <br/>
**Topic**: Pandas 1  <br/>
**Amount of time**: 1.5 hours <br/>
**Author**: Rachel Hirsch
​
​
***
​
## Lesson Summary:
​
#### Topic:
Introducing libraries: NumPy and Pandas
#### Learn.co material:
(link to github)
#### Prerequisite knowledge/ Prework:
Learn.co README files
#### Learning goals for this lesson:
SWBAT:
  - Identify and import Python libraries
  - Identify differences between NumPy and base Python in usage and operation
  - Import/read data using Pandas
  - Identify Pandas objects and manipulate Pandas objects by index and columns
  - Filter data using Pandas
#### Misconceptions:
(none filled out)

#### Materials
- Instructor jupyter notebook files (link here)
- Data set (https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238/data)
- Student jupyter notebook files (link here)

***

## Lesson Outline:

**Step**: Introduction and outline of lesson <br/>
**Time**: 2 min

_Goal/Scenario:_<br/>
Scenario: You have decided that you want to start your own animal shelter, but you want to get an idea of what that will entail and get more information about planning. You have found out that Austin has one of the largest no-kill animal shelters in the country, and they keep meticulous track of animals that have been taken in and released. However, it is a large file, the online visualization tools provided are terrible, the data is sorted as strings, and the file holds an overwhelming amount  of information. Is there an easy way to look at this data? Can we do this with base Python? Is there a better way?

In this lecture, we will discuss Python packages, specifically NumPy and Pandas, and use them to read in data, process data, and create basic plots with matplotlib.

_Learning Goals in sequence:_<br/>
- Identify and import Python libraries
- Identify differences between NumPy and base Python in usage and operation
- Import/read data with Pandas
- Identify Pandas objects and manipulate Pandas objects by index and columns
- Access and filter data using Pandas

**Step**: Activation <br/>
**Time**: 3 min

Discussion prompts:
share article about excel disaster
talk about why excel sucks




**Step**: Learning Goal 1: _Identify and import Python libraries_ <br/>
**Time**: 8 min

_Demonstrate_: 4 min <br/>
- Discuss python packages and their uses
- Introduce and discuss general uses of specific python packages (NumPy, SciPy) and import packages


_Application_: 3 min <br/>
- Students import packages
- Students run select package functions in jupyter notebook

_Informal assessment_: 1 min <br/>
"Quick fist of five check, how confident are we that we understand how to identify and import python packages? zero is not at all. five is ready to go."
- follow up with those students who do not feel confident

**Step**: Learning Goal 2: _Identify differences between NumPy and base Python in usage and operation_ <br/>
**Time**: 9 min

_Demonstrate_: 5 min <br/>
- Discuss differences between lists and arrays
- Import NumPy and run simple speed test on a small array
- Discuss memory differences between NumPy storage and base Python storage

_Application_: 3 min <br/>
- Students will create their own list and array of the three same numbers and attempt to divide them by 2
- Students will split into pairs, create varying sized arrays assigned by the instructor, and run a speed test on their assigned array
- Pairs will share the results with the class and compare results

_Informal assessment_: 1 min <br/>
"Thumbs up: I understand the differences between NumPy and base Python, thumbs down: I don't understand the differences, thumbs in the middle: I kind of understand the differences."
- follow up with any students who are not a thumbs up

**Step**: Learning Goal 3: _Import data sets with Pandas_ <br/>
**Time**: 6 min

_Demonstrate_: 3 min <br/>
- show how to import csv data without Pandas
- show different how to import csv data with Pandas and compare

_Application_: 2 min <br/>
- Students will import data using Pandas in different ways, including url
- Students will change commands to properly import data

_Informal assessment_: 1 min <br/>
"Thumbs up, down, or middle on importing data sets with Pandas."
- follow up with any non-thumbs up reponses

**Step**: Learning Goal 4: _Identify Pandas objects and manipulate Pandas objects by column and index_ <br/>
**Time**: 16 min

_Demonstrate_: 10 min <br/>
- Discuss series and dataframes, and show the difference between series and dataframes and lists and dictionaries
- Rename and drop columns using Pandas tools (df.rename, df.drop)
- Change/control indices in Pandas and compare to dictionaries and lists
- Change and control column data types
- Add a new column to the data frame and discuss SetWithCopyWarning

_Application_: 5 min <br/>
- Students will rename and drop columns from the resulting dataframe
- Students will change column data types in their dataframe
- Students will use iloc to add a new column of information to their dataframe


_Informal assessment_: 1 min <br/>
"Quick fist of five check, how confident are we that we understand the basics of pandas objects (series and dataframes)? zero is not at all. five is ready to go."
- follow up with students who do not feel confident

**Step**: Learning Goal 5: _Accessing and filtering data using Pandas_ <br/>
**Time**: 12 min

_Demonstrate_: 4 min <br/>
- Show how to access data by labels, indices, and columns
- Show how to perform boolean indexing on both Series and DataFrames
- Use simple selectors for series
- Set new Series and DataFrame inputs

_Application_: 7 min <br/>
- Students will pair together to explore the data using labels, boolean indexing, and selectors
- Students will change and set new values in series and dataframes

_Informal assessment_: 1 min <br/>
"Thumbs up, down, or middle on importing data sets with Pandas."
- follow up with any non-thumbs up responses

**Step**: Integration <br/>
Now that we have all of these new tools in our tool belt, let's take another look at our animal shelter data!

- check column names of dataset
- Drop columns from the animal shelter data until you have only 5 columns remaining
- rename those columns
- select rows of animals based on an application of boolean indexing.
- add in your own new column on information to this DataFrame.
 
**Step**: Assessment: poll stuff laterbr/>
**Time**: 15 min<br/>


**Step**: Reflection:  <br/>
**Time**: 5 min <br/>
- "What was one thing that you found challenging, one thing that surprised you, and one thing you found interesting?"
