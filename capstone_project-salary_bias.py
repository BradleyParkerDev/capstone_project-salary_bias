import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

employee_file = pd.read_csv('emp_file_CAPSTONE.txt')
# print(employee_file)

department_file = pd.read_csv('dept_CAPSTONE.txt')
# print(department_file)

raises_file = pd.read_csv('raises_CAPSTONE.txt')
# print(raises_file)

# You are a consulting firm tasked to examine the hiring practice of a division of a public company.
# You are given the HR records of all past and present employees. 
# A complaint has been filed that this division discriminates against women and low wage workers.  
# Examine the data and come up with a conclusion.
# The output should be in a jupyter notebook with the following name:
# Lastname_firstname_DATASCIENCE_CAPSTONE_202106
# Each answer should have a clear label of what you are answering using markdown




# Part 1-a
# 1 - Import employee file only the gender,salarly grade and dept columns
part_one_df = pd.DataFrame(data = employee_file, columns=['gender', 'sg', 'dept'])

# 2 - Fix the column dept capitalize it
part_one_df = part_one_df.rename(columns={'dept':'DEPT'})
print(part_one_df)

# 3 - Create a dataframe for every salary grade (index) with columns 'Male' and 'Female'
salary_grade_by_gender = part_one_df.groupby('sg')['gender'].value_counts().unstack().fillna(0)

print(salary_grade_by_gender)

dfs_by_sg = {}
for sg, sg_data in salary_grade_by_gender.iterrows():
    male_count = sg_data.get('M', 0)
    female_count = sg_data.get('F', 0)
    sg_df = pd.DataFrame({'Male': [male_count], 'Female': [female_count]})
    dfs_by_sg[sg] = sg_df

for sg, sg_df in dfs_by_sg.items():
    print(f"Salary Grade {sg}:")
    print(sg_df)


# 4 - Create pie charts for every Salary Grade with the ratio of men to women
for sg, sg_df in dfs_by_sg.items():
    # Extract male and female counts
    male_count = sg_df['Male'].values[0]
    female_count = sg_df['Female'].values[0]
    
    # Creates data for the pie chart
    data = [male_count, female_count]
    
    # Labels for the pie chart
    labels = ['Male', 'Female']
    
    # Creates pie charts
    plt.figure()
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Salary Grade {sg} - Men to Women Ratio')
    
    # Shows the pie charts
    plt.show()

# 5 - Create a dataframe for every Dept (index) with columns 'Male' and 'Female'

# Groups the part_one_df DataFrame by 'DEPT' (department) and 'gender', then get the counts
department_by_gender = part_one_df.groupby('DEPT')['gender'].value_counts().unstack().fillna(0)

# Creates a dictionary to store DataFrames for each department
dfs_by_dept = {}

# Loops through the departments and create DataFrames
for dept, dept_data in department_by_gender.iterrows():
    male_count = dept_data.get('M', 0)
    female_count = dept_data.get('F', 0)
    dept_df = pd.DataFrame({'Male': [male_count], 'Female': [female_count]})
    dfs_by_dept[dept] = dept_df

for dept, dept_df in dfs_by_dept.items():
    print(f"Department: {dept}")
    print(dept_df)
    print("\n")
# 6 - Create pie charts for every Dept with the ratio of men to women

# Loops through the DataFrames in dfs_by_dept and create pie charts
for dept, dept_df in dfs_by_dept.items():
    # Extract male and female counts
    male_count = dept_df['Male'].values[0]
    female_count = dept_df['Female'].values[0]
    
    # Creates data for the pie charts
    data = [male_count, female_count]
    
    # Labels for the pie chart
    labels = ['Male', 'Female']
    
    # Creates pie charts
    plt.figure()
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Department: {dept} - Men to Women Ratio')
    
    # Shows the pie charts
    plt.show() 
 



# NOTE - All charts should be automated


# Part 1-b
# 1 - Import employee file all columns
# 2 - Fix the case on the last name
# 3 - Create a field call Name which has the lastname, First name MI
# 4 - Create a alphabetic list of employees by last name, first name (Name)
# 5 - Create a alphabetic list of employees by last name, first name (Name) for each dept
# 6 - Create a horizontal bar chart with the number of employees per dept

# Part 2 - a
# 1 - Remove the NaN from the middle initial column
# 2 - Import the dept_CAPSTONE.txt file
# 3 - Make the deptCode all caps
# 4 - Remove the non alpha characters in the dept name
# 5 - Make the dept name each word initial caps
# 6 - Combine the emp_file and the dept_file and join both tables on dept code
# 7 - Create a file called ACTIVE_EMPLOYEES_BY_DEPT. Print list of all employees by dept by hire date (Descending order)
# 	with terminated employees eliminated
# 8 - Create a histogram that shows a count of the number of employees per dept by years employed


# Part 2 - b - SALARY ANALYSIS
# NOTE: A normal distribution has the following attributes:
# 68% within 1 standard deviation, 95% within 2 STD, 99% within 3 STD
# 1 - Decode the salaries containing 'X' according to the scale:

# 0 -->7
# 1 -->8
# 2 -->9
# 3 -->0
# 4 -->1
# 5 -->2
# 6 -->3
# 7 -->4
# 8 -->5
# 9 -->6

# 2 - Create a histogram of all salaries in deciles
# 3 - Calculate the mean, mode, median, and standard deviation of the salaries
# 4 - Is the salary distribution a normal distribution?
# 5 - Calculate the mean, mode, median, and standard deviation of the salaries of men
# 6 - Calculate the mean, mode, median, and standard deviation of the salaries of women
# 7 - Is the standard deviation, mean, mode, median higher for men? Calulate the % difference
# 8 - Write up- Do you think there is salary bias?


# Part 2 - c
# The salary grades of 5 - 7 are considered executive salary grades - Exempt or EXECUTIVE
# The salary grades of 1 - 4 are considered - Non-exempt (Hourly) - NON-EXECUTIVE
# 1 - create a new column called 'Status' Label each employee record in alpha order by name as EXEMPT or NON-EXEMPT
# 2 - Calculate the mean, mode, median, and standard deviation of the salaries of each salary grade
# 3 - Calculate the mean, mode, median, and standard deviation of the salaries of EXEMPT employees
# 4 - Calculate the mean, mode, median, and standard deviation of the salaries of NON-EXEMPT employees
# 5 - Create pie charts of the employee status of EXEMPT count by gender and NON-EXEMPT count by gender
# 6 - Create scatter plots of salary grade by mean salary
# 7 - Create a scatter plots of salary grade by mean salary for men
# 8 - Create a scatter plots of salary grade by mean salary for women
# 9 - Create a horizontal bar chart of EXEMPT employees by mean salary for men and women (1 chart)
# 10- Create a horizontal bar chart of NON-EXEMPT employees by mean salary for men and women (1 chart)
# 11 - Sort and output every Employee all columns by salary grade by name for every salary grade


# Part 3a - Create employee Id
# To construct the employee id for everyone use the following formula
# First 3 letters of the first name + first 3 letters of the last name + a random 3 digit number from (1 - 999) (edited) 
# For example the employee name is Kevin Smith id = 'SMIKEV007'
# In the case of people with the same last name and first name generate a new number
# No duplication
# 1 - List all employees in employee id order


# Part 3b -Raises
# 1 - Import the file raises_CAPSTONE.txt
# 2 - The rules for giving a raise are in the file but be careful of the order that your run the raise
# 3 - Based on each employees salary calculate 2 fields 'Raise_Amount' and 'New_Salary'
# 4 - Calculate the total salary for each dept
# 5 - Chart the total salary for each dept in 1 bar chart
# 6 - Create a pie chart that shows the percentage that each dept has of the total money allocated for raises
# 7 - Create a pie chart to show the percent of men vs women for the raise money allocated
# 8 - Create a pie chart to show the percent of men vs women for the raise money allocated by dept
# 9 - Create a dataframe for promotions.  If the persons salary excedes the salary max for their salary grade. create a column
# called 'Promotion' and add the string 'PROMOTION DUE' otherwise leave blank


# Part 4 - Analysis
# 1 - Write about any conclusions you drew from the data.
# 2 - Are there any additional charts or analysis you could include to bolster your conclusions