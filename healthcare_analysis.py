# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns


# Load Dataset
# Health_detect = pd.read_csv('/content/healthcare_dataset.csv')
Health_detect = pd.read_csv('healthcare_dataset.csv')

# Dataset First Look
Health_detect.head()

# Dataset Rows & Columns count
Health_detect.shape

# Dataset Info
Health_detect.info()

# Dataset Duplicate Value Count
duplicate_count = Health_detect.duplicated().sum()

duplicate_count

# Missing Values/Null Values Count
null_values = Health_detect.isnull().sum().reset_index()
null_values



# Visualizing the missing values
plt.plot(Health_detect.columns, Health_detect.isnull().sum(),marker='D',color='orange')
plt.xticks(rotation=90)
plt.grid()
plt.show()



#2

# Dataset Columns
print(Health_detect.columns)

# Dataset Describe
Health_detect.describe()

# Check Unique Values for each variable.
unique_values = Health_detect.nunique().reset_index()
unique_values

#3

# Renaming Column
Health_detect = Health_detect.rename(columns={'Billing Amount': 'Billing_Amount'})
Health_detect.describe()

# Standardisation of billing amount
Health_detect['Billing_Amount_Standardized'] = (Health_detect['Billing_Amount'] - Health_detect['Billing_Amount'].mean()) / Health_detect['Billing_Amount'].std()
Health_detect['Billing_Amount_Standardized']

# Group by Gender and calculate average billing amount
average_billing_by_gender = Health_detect.groupby('Gender')['Billing_Amount'].mean()
print("Average Billing Amount by Gender:\n", average_billing_by_gender)


# Group by Medical Condition and count number of occurrences
medical_condition_counts = Health_detect.groupby('Medical Condition').size()
print("\nMedical Condition Counts:\n", medical_condition_counts)


#Find total days of stay
Health_detect['Date of Admission'] = pd.to_datetime(Health_detect['Date of Admission'])
Health_detect['Discharge Date'] = pd.to_datetime(Health_detect['Discharge Date'])

Health_detect['Length of Stay'] = (Health_detect['Discharge Date'] - Health_detect['Date of Admission']).dt.days
Health_detect['Length of Stay']


# Group by Admission Type and calculate total billing amount
total_billing_by_admission_type = Health_detect.groupby('Admission Type')['Billing_Amount'].sum()
print("\nTotal Billing Amount by Admission Type:\n", total_billing_by_admission_type)


#4

female_data = Health_detect[Health_detect['Gender'] == 'Female']

# Count the occurrences of each medical condition among women
medical_condition_counts = female_data['Medical Condition'].value_counts()

# Plot the bar graph
plt.figure(figsize=(10, 6))
medical_condition_counts.plot(kind='bar', color='orange')
plt.xlabel('Medical Condition')

plt.ylabel('Frequency')
plt.title('Distribution of Medical Conditions Among Women')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the bar graph
plt.show()

# Chart - 2 visualization code
Health_detect['Medical Condition'].value_counts().plot.pie(autopct='%1.2f%%',explode=[0,0,0,0,0,0.1])
plt.show()

111# Chart - 3 visualization code
sns.countplot(x='Medical Condition', hue='Gender', data=Health_detect, palette=['orange','purple'])
plt.title('Distribution of Medical Diseases by Gender')

plt.legend(title='Gender', loc='upper right')
plt.show()

admission_type_counts = Health_detect['Admission Type'].value_counts()

# Plot the bar plot
plt.figure(figsize=(10, 6))
admission_type_counts.plot(kind='bar', color='orange')
plt.xlabel('Admission Type')
plt.ylabel('Frequency')
plt.title('Distribution of Admission Types')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the bar plot
plt.show()

test_results_counts = Health_detect['Test Results'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(test_results_counts, labels=test_results_counts.index, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Distribution of Test Results')

plt.show()


avg_billing_by_condition = Health_detect.groupby('Medical Condition')['Billing_Amount'].mean()

# Bar plot
avg_billing_by_condition.plot.bar(color='ORANGE')
plt.xlabel('Medical Condition')
plt.ylabel('Average Billing Amount')
plt.title('Average Billing Amount by Medical Condition')
plt.show()


arthritis_patients = Health_detect[Health_detect['Medical Condition'] == 'Arthritis']

# Count occurrences of each gender
gender_counts = arthritis_patients['Gender'].value_counts()

# Set up the pie chart
plt.figure(figsize=(8, 8))

# Create pie chart
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Distribution of Arthritis Patients by Gender')

# Show plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


test_results_counts = Health_detect['Test Results'].value_counts()

# Create a horizontal bar graph
plt.figure(figsize=(8, 6))
test_results_counts.plot(kind='barh', color='pink')

# Adding labels and title
plt.xlabel('Frequency')
plt.ylabel('Test Result')
plt.title('Distribution of Test Results')

plt.show()



plt.figure(figsize=(10, 6))

# Create countplot with horizontal orientation and sorted by frequency
sns.countplot(data=Health_detect, y='Medical Condition', palette='viridis', order=Health_detect['Medical Condition'].value_counts().index)

# Add labels and title
plt.xlabel('Frequency')
plt.ylabel('Medical Condition')
plt.title('Distribution of Medical Conditions')

# Show plot
plt.show()


import matplotlib.pyplot as plt


ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create histogram
plt.hist(ages, bins=10, color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

# Show plot
plt.show()



blood_type_counts = Health_detect['Blood Type'].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(blood_type_counts, labels=blood_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Blood Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Show the pie chart
plt.show()


medication_counts = Health_detect['Medication'].value_counts()

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(Health_detect['Medication'], bins=len(medication_counts), color='orange', edgecolor='black')
plt.xlabel('Medication')
plt.ylabel('Frequency')
plt.title('Distribution of Medications')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Show the histogram
plt.show()



male_data = Health_detect[Health_detect['Gender'] == 'Male']

# Count the occurrences of each medical condition among men
medical_condition_counts = male_data['Medical Condition'].value_counts()

# Create a line graph
plt.figure(figsize=(10, 6))
plt.plot(medical_condition_counts.index, medical_condition_counts.values, marker='o', color='skyblue', linestyle='-')
plt.xlabel('Medical Condition')
plt.ylabel('Frequency')
plt.title('Distribution of Medical Conditions Among Men')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the line graph
plt.show()



# Correlation Heatmap visualization code
# Convert Date columns to datetime
Health_detect['Date of Admission'] = pd.to_datetime(Health_detect['Date of Admission'])
Health_detect['Discharge Date'] = pd.to_datetime(Health_detect['Discharge Date'])

# Calculate correlation matrix
correlation_matrix = Health_detect.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Dataset')
plt.show()



# Pair Plot visualization code
Health_detect['Date of Admission'] = pd.to_datetime(Health_detect['Date of Admission'])
Health_detect['Discharge Date'] = pd.to_datetime(Health_detect['Discharge Date'])

# Convert categorical variables to categorical data type
categorical_cols = ['Gender', 'Blood Type', 'Medical Condition', 'Doctor', 'Hospital', 'Insurance Provider', 'Admission Type', 'Medication', 'Test Results']
for col in categorical_cols:
    Health_detect[col] = Health_detect[col].astype('category')

# Plot pair plot
sns.pairplot(Health_detect)
plt.suptitle('Pair Plot of Dataset', y=1.02)
plt.show()





