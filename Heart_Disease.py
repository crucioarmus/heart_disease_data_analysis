import pandas as pd
data =pd.read_csv("heart_disease.csv") #would create a data frame
#######STEP1 --UNDERSTANDING DATA---

print(data.head()) #first 5 records
print("\n Data Size")
print(data.shape) #size of dataset
print("\n Coloumns")
print(data.columns) #displays all feature or coloumns 
print("\n info")
print(data.info()) #dtypes,null values of features
print("\n stats")
print(data.describe()) #basic stat of dataset e.g mean,count,std etc


####STEP 2---DATA CLEANING----

print("\n MISSING VALUES IN EACH COLOUMN")
print(data.isnull().sum())
print("\nDuplicates")
print(data.duplicated().sum())
##replacing the missing values w mean
data["Age"]=data["Age"].fillna(data["Age"].mean())
data["Gender"]=data["Gender"].fillna(data["Gender"].mode()[0])  ###non numeric dtype
data["Blood Pressure"]=data["Blood Pressure"].fillna(data["Blood Pressure"].mean())
data["Cholesterol Level"]=data["Cholesterol Level"].fillna(data["Cholesterol Level"].mean())
data["Exercise Habits"]=data["Exercise Habits"].fillna(data["Exercise Habits"].mode()[0])
data["Smoking"]=data["Smoking"].fillna(data["Smoking"].mode()[0])
data["Family Heart Disease"]=data["Family Heart Disease"].fillna(data["Family Heart Disease"].mode()[0])
data["Diabetes"]=data["Diabetes"].fillna(data["Diabetes"].mode()[0])

# Numeric columns
data["BMI"] = data["BMI"].fillna(data["BMI"].mean())
data["Sleep Hours"] = data["Sleep Hours"].fillna(data["Sleep Hours"].mean())
data["Triglyceride Level"] = data["Triglyceride Level"].fillna(data["Triglyceride Level"].mean())
data["Fasting Blood Sugar"] = data["Fasting Blood Sugar"].fillna(data["Fasting Blood Sugar"].mean())
data["CRP Level"] = data["CRP Level"].fillna(data["CRP Level"].mean())
data["Homocysteine Level"] = data["Homocysteine Level"].fillna(data["Homocysteine Level"].mean())

# Categorical columns
data["High Blood Pressure"] = data["High Blood Pressure"].fillna(data["High Blood Pressure"].mode()[0])
data["Low HDL Cholesterol"] = data["Low HDL Cholesterol"].fillna(data["Low HDL Cholesterol"].mode()[0])
data["High LDL Cholesterol"] = data["High LDL Cholesterol"].fillna(data["High LDL Cholesterol"].mode()[0])
data["Alcohol Consumption"] = data["Alcohol Consumption"].fillna(data["Alcohol Consumption"].mode()[0])
data["Stress Level"] = data["Stress Level"].fillna(data["Stress Level"].mode()[0])
data["Sugar Consumption"] = data["Sugar Consumption"].fillna(data["Sugar Consumption"].mode()[0])

print(data.isnull().sum())

##STEP 3------SELECTING AND FILTERING THE DATA-------
data[["Age","Low HDL Cholesterol"]] ##SELECTING MULTIPLE COLUMNS
print(data[data["Age"]>60]) ##filtering the rows
print(data[(data["Age"]>60) & (data["Gender"] == "Male")]) #Multiple conditions



print(data["Smoking"].unique()) #displays the value that exist in this coloumn

print(data["Smoking"].value_counts())

print(data["Heart Disease Status"].unique())
print(data["Heart Disease Status"].value_counts())

#stage 04----DATA ANALYSIS------
print(data.groupby("Gender")) ###groups the dataset by gender
print(data.groupby("Gender")["Age"].mean()) ##mean age of each group

print(data.groupby("Gender")["Cholesterol Level"].mean())

print(data.groupby("Heart Disease Status")["BMI"].mean())

print(data.groupby("Smoking")["Heart Disease Status"].value_counts())

import matplotlib.pyplot as plt

plt.hist(data["Age"], bins=20, color="skyblue", edgecolor="black", density=True)
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

data["Gender"].value_counts().plot(kind="bar", color = "lightcoral")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")

plt.show()


pd.crosstab(data["Smoking"], data["Heart Disease Status"],normalize="index").plot(kind="bar")

plt.title("Smoking vs Heart Disease")
plt.xlabel("Smoking Status")
plt.ylabel("Number of Patients")

plt.show()
print(data["Heart Disease Status"].value_counts())



