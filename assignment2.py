# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HBpGFGAyE_41-OsoQ0w5WlQz7enP-2Um
"""

"""Load the data from a CSV file into memory using the pandas module. The 
path to the file will be specified by the user then use these loaded data to
perform following tasks"""
import pandas as pd
df = pd.read_csv('C:\\Users\\MVSR\\Desktop\\Dataset.csv')
print("loaded")

###Identifying the most popular amenities or features that Airbnb guests are looking for
###  The pandas value_counts() function is used to get the count of each unique value in a pandas series. You can use it to get the counts and then extract the value with the most counts using idxmax() function.
print("The most popular aminities that Airbnb guests are looking are :")
df['amenities'].value_counts().idxmax()

###Analyse the average price of stay in each location
#### Calculating mean on groupby
avgprice = df.groupby('host_location')['price'].mean()
###To print all the values
print("The average price of stay in each location are:")
print(avgprice.to_string())

###analse the average review score for each location
avgreview = df.groupby('host_location')['review_scores_rating'].mean()
print("the average review score for each location are:")
print(avgreview.to_string())

#Analyse to get insightful information based on your own selection (should not be the same as the previous requirements)
avgbedrooms = df.groupby('host_location')['bedrooms'].mean()
print("the average bedrooms for each location are:")
print(avgbedrooms.to_string())