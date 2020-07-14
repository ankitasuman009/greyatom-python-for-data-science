# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)
print(data.iloc[25, 1])
# df = pd.DataFrame(data)
#Code starts here
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar')
# # Step 1 
#Reading the file

property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
#Creating a new variable to store the value counts
property_and_loan = property_and_loan.size().unstack()
property_and_loan = property_and_loan.plot(kind = 'bar', stacked = False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)
plt.show()

#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack().plot(kind = 'bar', stacked = True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)
plt.show()

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

graduate = pd.DataFrame(data[data['Education'] == 'Graduate'])
not_graduate = pd.DataFrame(data[data['Education'] == 'Not Graduate']) 

#Changing the x-axis label
pd.Series(graduate['LoanAmount']).plot(kind = 'density', label = 'Graduate')
pd.Series(not_graduate['LoanAmount']).plot(kind = 'density', label = 'Not Graduate')
#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)

#Subsetting the dataframe based on 'Education' column
data.plot.scatter(x= 'ApplicantIncome', y = 'LoanAmount', ax = ax_1)
ax_1.set_title('Applicant Income')

# #Plotting density plot for 'Graduate'
data.plot.scatter(x = 'CoapplicantIncome', y = 'LoanAmount', ax = ax_2)
ax_2.set_title('Coapplicant Income')

#Plotting density plot for 'Graduate'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x = 'TotalIncome', y = 'LoanAmount', ax = ax_3)
ax_3.set_title('Total Income')
#For automatic legend display
print(data['TotalIncome'][1])

# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



