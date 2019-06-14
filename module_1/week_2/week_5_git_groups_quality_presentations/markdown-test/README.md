# Predicting tomorrow's rainfall in Australia

## Executive summary

The goal of this analysis is to predict whether it will rain tomorrow in a given city in Australia, based on today's weather. We analyzed a Kaggle dataset of daily weather data collected in 49 Australian cities between 2010 and 2018. The final model had an 83.9% accuracy rate in predicting whether or not it would rain tomorrow vs. a baseline model accuracy of 77.8%.

![Rainfall in Australia Map](rainfall_map.png)

## Contents

- [Introduction](#Introduction)
    - [Problem statement](#Problem-statement)
    - [Dataset](#Dataset)
- [Analysis](#Analysis)
    - [Data cleaning](#Data-cleaning)
    - [Exploratory data analysis](#Exploratory-data-analysis)
    - [Modeling](#Modeling)
    - [Metrics](#Metrics)
- [Next steps](#Next-steps)


## Introduction

### Problem statement

Our goal is to predict whether or not it will rain tomorrow, in a given city in Australia, based on today's weather, using replicable machine learning techniques. We used two separate modeling techniques (Decision Tree and Random Forest) to create these forecasts.

### Dataset

The analysis is based on this [Kaggle dataset](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package) of **daily weather data** collected in 49 Australian cities between 2010 and 2018. *The dataset consists of 22 numerical and categorical features, and 1 target classification variable.*

## Analysis

### Data cleaning

We had duplicate data, missing values, and impossible values that we had to rectify before proceeding to modeling.

### Exploratory data analysis

We found some signficant correlations in our data that we had to explore further.

### Modeling

Our analysis used both Decision Tree and Random Forest classifier models.

We can create multiline Python code with syntax highlighting:

```python

def model():
    for kind in models:
        start = time.time()
        if kind == 'Tree':
            model = tree.DecisionTreeClassifier()
        else : 
            model = ensemble.RandomForestClassifier()
```

### Metrics

We create a confusion matrix to calculate classification metrics using the `sklearn.metrics.confusion_matrix()` method.

## Next Steps

![Bran](https://i.imgur.com/3fkDIms.jpg)
