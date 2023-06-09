# -*- coding: utf-8 -*-
"""Assignment3 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_m6S5HjdC-1R5y-Q4xFEhLo0uSHvUFV
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:\\Users\\MVSR\\Desktop\\Dataset.csv')

###Display the proportion of number of bedrooms of Airbnb listing using pie chart
###let’s first sort the indices and counts for our bedroom column:
label=df.bedrooms.value_counts().index
count=df.bedrooms.value_counts().values
###TO enlarge our chart to view it clearly figsize parameter in the figure() function to set the dimensions of the figure in inches.

###plt.figure(1, figsize=(20,10))
##pie chart
plt.pie(count,labels=label)

###Use plt.title() for setting a plot title
###Use plt.legend() for the observation variables
###Use plt.show() for displaying the plot
plt.title('Proportion of bedrooms')
plt.legend()
plt.show()

###Display the number of listings for each room type using bar chart
df['room_type'].value_counts().plot(kind='bar')

###Display the relationship between accommodates and price using scatter plot
#import seaborn as sns
subplot=df[['accommodates','price']]
scatter=subplot.plot(x ='accommodates', y = 'price', kind='scatter', c='green');
scatter.set_title('Relationship between accommodates and price');
scatter.figure.savefig('Relationship.png')
#sns.scatterplot(x="accommodates", y="price", data=df);

###Display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot)
# Make a list of columns
import datetime
#import seaborn as sns
# convert the host_since Date to datetime
df["host_since"]= pd.to_datetime(df["host_since"])
## add a column for Year to store only 'year'
df['Year'] = df['host_since'].dt.strftime('%Y')
df['Year']
#extract the year from 2019 to 2022 and strore in year1
Year1=pd.DataFrame(df.loc[(df['Year']>='2019')&(df['Year']<='2022')])
Year1.columns

plt.plot(Year1['Year']=='2019',Year1['price'],color='g',label='2019')
plt.xlabel("year  2019")
plt.ylabel("price") 
plt.legend()
plt.show()

fig,ax=plt.subplots(1,4,sharey=True)
plt.subplot(141)
plt.plot(Year1['Year']=='2019',Year1['price'],color='g',label='2019')
plt.xlabel("year  2019")
plt.subplot(142)
plt.plot(Year1['Year']=='2020',Year1['price'],color='g',label='2020')
plt.xlabel("year  2020")
plt.subplot(143)
plt.plot(Year1['Year']=='2021',Year1['price'],color='g',label='2021')
plt.xlabel("year  2021")
plt.subplot(144)
plt.plot(Year1['Year']=='2022',Year1['price'],color='g',label='2022')
plt.xlabel("year  2022")
plt.ylabel("price") 
plt.legend()
plt.show()

#Year1['bedrooms'].plot(kind="hist",bins=5)
fig.ax=plt.subplots(figsize=(5,5))
plt.hist(Year1['bedrooms'],bins=5)



