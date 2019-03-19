# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:47:49 2018

@author: Jigyasa Yadav
"""

#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#loading data in dataframe
Data=pd.read_csv("Data.csv")

#handing missing values
Data = Data.fillna(Data.mean())

#grouping by state_name
state=Data.groupby('State_Name')

#mean, median  of state population
st1 = Data['Population_Total'].mean()
st2 = Data['Population_Total'].median()

#max population among different districts
m1 = Data['Population_Total'].max()

#sum of values statewise
states_no=state.sum()

#max population among different states
m2 = states_no['Population_Total'].max()

#counting no. of district in each state
x = Data['State_District_Name'].count()

#swarmplots
sns.swarmplot(y='State_Name',x='Infant_Mortality_Rate_Imr_Total_Person',data=Data)

sns.swarmplot(x='Sex_Ratio_At_Birth_Urban',y='Sex_Ratio_At_Birth_Rural',data=Data,hue='State_Name')

#piechart for popuation percentage
cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]
pie_sources = Data.groupby('State_Name').agg('count')
source_labels = pie_sources.Population_Total.sort_values().index
source_counts = pie_sources.Population_Total.sort_values()
plt.pie(source_counts, labels=source_labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=20)
plt.axis('equal')
fig=plt.title('Population percentage of the mentioned states')

#bxplot for crude_death rate
sns.set(rc={'figure.figsize':(10,5)})
sns.boxplot(x="State_Name", y="Crude_Death_Rate_Cdr_Total_Person", data=Data)

#
sns.distplot(Data['Marriages_Among_Females_Below_Legal_Age_18_Years_Rural'], bins=30,kde=False)

#
sns.jointplot(x='Infant_Mortality_Rate_Imr_Total_Female',y='Infant_Mortality_Rate_Imr_Total_Male',data=Data,kind='reg')

#barplot for dependency ratio in rural& urban
Factor=['Assam','Bihar','Chhattisgarh','Jharkhand','Madhya Pradesh','Odisha','Rajasthan','Uttar Pradesh','Uttarakhand']
y=states_no['Dependency_Ratio_Urban']
sns.barplot(x=Factor, y=y.values,  data=Data)

x=states_no['Dependency_Ratio_Rural']
sns.barplot(x=Factor, y=x.values,  data=Data)

#jointplot for Currently_Married_Illiterate_Women_Aged_15_49_Years
sns.jointplot(x='Currently_Married_Illiterate_Women_Aged_15_49_Years_Rural',y='Currently_Married_Illiterate_Women_Aged_15_49_Years_Urban',data=Data,kind='reg')

#pie chart for Children_Currently_Attending_School_Age_6_17_Years_Person_Total
cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]
pie_sources = Data.groupby('State_Name').agg('count')
source_labels = pie_sources.Children_Currently_Attending_School_Age_6_17_Years_Person_Total.sort_values().index
source_counts = pie_sources.Children_Currently_Attending_School_Age_6_17_Years_Person_Total.sort_values()
plt.pie(source_counts, labels=source_labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=20)
plt.axis('equal')
fig=plt.title('Children_Currently_Attending_School_Age_6_17_Years_Person_Total')

#distplot for children engaged in work
sns.distplot(Data['Children_Aged_5_14_Years_Engaged_In_Work_Person_Total'], bins=30,kde=False)

#distplot for disability 
sns.distplot(Data['Prevalence_Of_Any_Type_Of_Disability_Per_100000_Population_Person_Total'], bins=30,kde=False)

#boxplot for Children_Who_Did_Not_Receive_Any_Vaccination_Rural 
sns.set(rc={'figure.figsize':(10,5)})
sns.boxplot(x="State_Name", y="Children_Who_Did_Not_Receive_Any_Vaccination_Rural", data=Data)

#
sns.set(rc={'figure.figsize':(10,5)})
sns.boxplot(x="State_Name", y="Children_Who_Did_Not_Receive_Any_Vaccination_Urban", data=Data)

#
Factor=['Assam','Bihar','Chhattisgarh','Jharkhand','Madhya Pradesh','Odisha','Rajasthan','Uttar Pradesh','Uttarakhand']
y=states_no['Children_Aged_5_14_Years_Engaged_In_Work_Person_Total']
sns.barplot(x=Factor, y=y.values,  data=Data)