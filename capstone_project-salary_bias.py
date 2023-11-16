import pandas as pd
import numpy as np
import statistics as stats
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




# # Part 1-a
# # 1 - Import employee file only the gender,salarly grade and dept columns
# part_one_df = pd.DataFrame(data = employee_file, columns=['gender', 'sg', 'dept'])

# # 2 - Fix the column dept capitalize it
# part_one_df = part_one_df.rename(columns={'dept':'DEPT'})
# print(part_one_df)

# # 3 - Create a dataframe for every salary grade (index) with columns 'Male' and 'Female'
# salary_grade_by_gender = part_one_df.groupby('sg')['gender'].value_counts().unstack().fillna(0)

# print(salary_grade_by_gender)

# dfs_by_sg = {}
# for sg, sg_data in salary_grade_by_gender.iterrows():
#     male_count = sg_data.get('M', 0)
#     female_count = sg_data.get('F', 0)
#     sg_df = pd.DataFrame({'Male': [male_count], 'Female': [female_count]})
#     dfs_by_sg[sg] = sg_df

# for sg, sg_df in dfs_by_sg.items():
#     print(f"Salary Grade {sg}:")
#     print(sg_df)


# # 4 - Create pie charts for every Salary Grade with the ratio of men to women
# for sg, sg_df in dfs_by_sg.items():
#     # Extract male and female counts
#     male_count = sg_df['Male'].values[0]
#     female_count = sg_df['Female'].values[0]
    
#     # Creates data for the pie chart
#     data = [male_count, female_count]
    
#     # Labels for the pie chart
#     labels = ['Male', 'Female']
    
#     # Creates pie charts
#     plt.figure()
#     plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
#     plt.title(f'Salary Grade {sg} - Men to Women Ratio')
    
#     # Shows the pie charts
#     plt.show()

# # 5 - Create a dataframe for every Dept (index) with columns 'Male' and 'Female'

# # Groups the part_one_df DataFrame by 'DEPT' (department) and 'gender', then get the counts
# department_by_gender = part_one_df.groupby('DEPT')['gender'].value_counts().unstack().fillna(0)

# # Creates a dictionary to store DataFrames for each department
# dfs_by_dept = {}

# # Loops through the departments and create DataFrames
# for dept, dept_data in department_by_gender.iterrows():
#     male_count = dept_data.get('M', 0)
#     female_count = dept_data.get('F', 0)
#     dept_df = pd.DataFrame({'Male': [male_count], 'Female': [female_count]})
#     dfs_by_dept[dept] = dept_df

# for dept, dept_df in dfs_by_dept.items():
#     print(f"Department: {dept}")
#     print(dept_df)
#     print("\n")
# # 6 - Create pie charts for every Dept with the ratio of men to women

# # Loops through the DataFrames in dfs_by_dept and create pie charts
# for dept, dept_df in dfs_by_dept.items():
#     # Extract male and female counts
#     male_count = dept_df['Male'].values[0]
#     female_count = dept_df['Female'].values[0]
    
#     # Creates data for the pie charts
#     data = [male_count, female_count]
    
#     # Labels for the pie chart
#     labels = ['Male', 'Female']
    
#     # Creates pie charts
#     plt.figure()
#     plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
#     plt.title(f'Department: {dept} - Men to Women Ratio')
    
#     # Shows the pie charts
#     plt.show() 
 



# NOTE - All charts should be automated


# # Part 1-b
# # 1 - Import employee file all columns
# print(employee_file)




# # 2 - Fix the case on the last name
employee_file['ln'] = employee_file['ln'].str.title()
# print(employee_file)



# # 3 - Create a field call Name which has the lastname, First name MI
# employee_file['Name'] = employee_file['ln'] + ', ' + employee_file['fn'] + ' ' + employee_file['mi'].fillna('')
# print(employee_file)




# # 4 - Create a alphabetic list of employees by last name, first name (Name)
# sorted_employee_list = employee_file.sort_values(by=['ln', 'fn'])
# print(sorted_employee_list)


# # 5 - Create a alphabetic list of employees by last name, first name (Name) for each dept
# sorted_employee_lists_by_dept = {}

# for dept, group in employee_file.groupby('dept'):
#     sorted_group = group.sort_values(by=['ln', 'fn'])
#     sorted_group.reset_index(drop=True, inplace=True)  # Reset the index to start from 0
#     sorted_employee_lists_by_dept[dept] = sorted_group

# for dept, sorted_employee_list in sorted_employee_lists_by_dept.items():
#     print(f"Department: {dept}")
#     print(sorted_employee_list)
#     print("\n")

# # 6 - Create a horizontal bar chart with the number of employees per dept

# # Group the employees by department and count the number of employees in each department
# dept_employee_counts = employee_file['dept'].value_counts()

# # Create a horizontal bar chart
# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# dept_employee_counts.plot(kind='barh', color='skyblue')
# plt.xlabel('Number of Employees')
# plt.ylabel('Department')
# plt.title('Number of Employees per Department')

# # Show the bar chart
# plt.show()









# Part 2 - a
# 1 - Remove the NaN from the middle initial column
employee_file['mi'].fillna('', inplace=True)
# print(employee_file)
# 2 - Import the dept_CAPSTONE.txt file
# print(department_file)

# 3 - Make the deptCode all caps
department_file.columns = department_file.columns.str.replace("'", "")
department_file['deptCode'] = department_file['deptCode'].str.upper()
# print(department_file)

# 4 - Remove the non alpha characters in the dept name
department_file['dept name'] = department_file['dept name'].str.replace("[^a-zA-Z\s]", "", regex=True)
# print(department_file)

# 5 - Make the dept name each word initial caps
department_file['dept name'] = department_file['dept name'].str.title()
# print(department_file)

# 6 - Combine the emp_file and the dept_file and join both tables on dept code

# removes single quotes from deptCode values, and creates a dict from the department_file
department_file['deptCode'] = department_file['deptCode'].str.replace("'", "")
dept_dict = dict(zip(department_file['deptCode'], department_file['dept name']))
# print(dept_dict)

# combines the employee_file and department_file on the dept code
employee_file['dept'] = employee_file['dept'].str.upper()
combined_data = pd.merge(employee_file, department_file, left_on='dept', right_on='deptCode', how='left')
combined_data = combined_data.drop('deptCode', axis=1)
combined_data['dept name'] = combined_data['dept'].map(dept_dict)


# print(combined_data)

 

# 7 - Create a file called ACTIVE_EMPLOYEES_BY_DEPT. Print list of all employees by dept by hire date (Descending order)
# 	with terminated employees eliminated
# Filter out terminated employees

# Creates an active_employees data frame
combined_data.loc[combined_data['termdate'].apply(lambda x: len(str(x)) <= 1), 'termdate'] = ""
active_employees = combined_data[combined_data['termdate'].apply(lambda x: len(str(x)) <= 1)]
active_employees['hiredate'] = pd.to_datetime(active_employees['hiredate'], format='%m/%d/%Y')

# Creates dictionary of  dataframes with active employees by department
active_by_dept_data = {}
for dept, group in active_employees.groupby('dept'):
    sorted_group = group.sort_values(by='hiredate', ascending=False)
    sorted_group.reset_index(drop=True, inplace=True)  # Reset the index to start from 0
    active_by_dept_data[dept] = sorted_group

# Creates one dataframe with employees by dept by hire date (Descending order)
active_employees = pd.concat(active_by_dept_data.values(), ignore_index=True)
# print(active_employees)

# Creates csv file
active_employees.to_csv('ACTIVE_EMPLOYEES_BY_DEPT.csv', index=False)


# 8 - Create a histogram that shows a count of the number of employees per dept by years employed

# Step 1: Calculate years employed
# active_employees['hiredate'] = pd.to_datetime(active_employees['hiredate'])  # Ensure 'hiredate' is in datetime format
# active_employees['years_employed'] = (pd.to_datetime('today') - active_employees['hiredate']).dt.days // 365

# # Step 2: Create a histogram
# plt.figure(figsize=(10, 6))
# for dept, group in active_employees.groupby('dept'):
#     plt.hist(group['years_employed'], bins=20, alpha=0.7, label=dept)

# plt.title('Number of Employees per Department by Years Employed')
# plt.xlabel('Years Employed')
# plt.ylabel('Number of Employees')
# plt.legend()
# plt.grid(True)
# plt.show()

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

decode_mapping = {
    '0': 7,
    '1': 8,
    '2': 9,
    '3': 0,
    '4': 1,
    '5': 2,
    '6': 3,
    '7': 4,
    '8': 5,
    '9': 6
}

def decode_salary(salary_str):
    # Remove dollar sign and then find the position of 'X' in the string
    salary_str = salary_str.replace('$', '')
    x_position = salary_str.find('X')
    
    if x_position != -1:
        decoded_str = ''.join(str(decode_mapping[digit]) for digit in salary_str[x_position + 1:])
        return int(decoded_str)
    else:
        return int(salary_str)

# Apply the decoding function to the 'salary' column
active_employees['decoded_salary'] = active_employees['salary'].astype(str).apply(decode_salary)
active_employees['salary'] = active_employees['decoded_salary']
active_employees.drop('decoded_salary', axis=1, inplace=True)
print(active_employees)

# 2 - Create a histogram of all salaries in deciles


# # Defines the number of bins
# num_bins = 10

# # Creates salary bins
# salary_bins = np.linspace(active_employees['salary'].min(), active_employees['salary'].max(), num_bins + 1)

# # Creates histogram
# plt.figure(figsize=(10, 6))
# plt.hist(active_employees['salary'], bins=salary_bins, color='blue', alpha=0.7, rwidth=0.85)
# plt.title('Histogram of Salaries with 10 Bins')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# # Labels x-axis with salary ranges
# bin_labels = [f'${int(salary_bins[i])}-{int(salary_bins[i+1])}' for i in range(len(salary_bins)-1)]
# plt.xticks(salary_bins[:-1], bin_labels, rotation=45, ha='right')  # Adjust here

# plt.show()



# 3 - Calculate the mean, mode, median, and standard deviation of the salaries

# Calculate mean, mode, median, and standard deviation
mean_salary = np.mean(active_employees['salary'])
mode_salary = stats.mode(active_employees['salary'])
median_salary = np.median(active_employees['salary'])
std_dev_salary = np.std(active_employees['salary'])

# Print the results
print(f"Mean Salary: ${mean_salary:.2f}")
print(f"Mode Salary: ${mode_salary:.2f}")
print(f"Median Salary: ${median_salary:.2f}")
print(f"Standard Deviation of Salary: ${std_dev_salary:.2f}")

# 4 - Is the salary distribution a normal distribution?

"""
The salary distribution is skewed to the right, 
and salaries begin to visibly decline after the 
fifth bin in the histogram.  
A marjority of people are paid within the salary range of
$21,875 and $243,309; there are visibly fewer people being paid more than this.

"""


# 5 - Calculate the mean, mode, median, and standard deviation of the salaries of men
print()
# Filters the DataFrame for male employees
male_salaries = active_employees[active_employees['gender'] == 'M']['salary']

# Calculates mean, mode, median, and standard deviation
mean_salary_male = stats.mean(male_salaries)
mode_salary_male = stats.mode(male_salaries)
median_salary_male = stats.median(male_salaries)
std_dev_salary_male = stats.stdev(male_salaries)

# Prints the results
print(f"Mean Salary of Men: ${mean_salary_male}")
print(f"Mode Salary of Men: ${mode_salary_male}")
print(f"Median Salary of Men: ${median_salary_male}")
print(f"Standard Deviation of Salary of Men: ${std_dev_salary_male}")

# 6 - Calculate the mean, mode, median, and standard deviation of the salaries of women
print()

# Filters the DataFrame for female employees
female_salaries = active_employees[active_employees['gender'] == 'F']['salary']

# Calculates mean, mode, median, and standard deviation
mean_salary_female = stats.mean(female_salaries)
mode_salary_female = stats.mode(female_salaries)
median_salary_female = stats.median(female_salaries)
std_dev_salary_female = stats.stdev(female_salaries)

# Prints the results
print(f"Mean Salary of Women: ${mean_salary_female}")
print(f"Mode Salary of Women: ${mode_salary_female}")
print(f"Median Salary of Women: ${median_salary_female}")
print(f"Standard Deviation of Salary of Women: ${std_dev_salary_female}")

# 7 - Is the standard deviation, mean, mode, median higher for men? Calulate the % difference
print()

# Calculate the percentage differences
mean_diff_percent = ((mean_salary_male - mean_salary_female) / mean_salary_female) * 100
mode_diff_percent = ((mode_salary_male - mode_salary_female) / mode_salary_female) * 100
median_diff_percent = ((median_salary_male - median_salary_female) / median_salary_female) * 100
std_dev_diff_percent = ((std_dev_salary_male - std_dev_salary_female) / std_dev_salary_female) * 100

# Print the results
print("Mean Salary Difference (%):",mean_diff_percent)
print("Mode Salary Difference (%):",mode_diff_percent)
print("Median Salary Difference (%):",median_diff_percent)
print("Standard Deviation Difference (%):",std_dev_diff_percent)


# 8 - Write up- Do you think there is salary bias?
"""
I think there might be a bias towards women. The mean and median salaries 
of women are higher than those of males. Their standard
deviation is also around 10% lower than the males--which means their 
salaries dont deviate as much from their mean salary. However, it's crucial 
to consider that males constitute a majority of the employees in the organization, 
and the sample size should be taken into account when drawing conclusions.
"""

# Part 2 - c
# The salary grades of 5 - 7 are considered executive salary grades - Exempt or EXECUTIVE
# The salary grades of 1 - 4 are considered - Non-exempt (Hourly) - NON-EXECUTIVE
# 1 - create a new column called 'Status' Label each employee record in alpha order by name as EXEMPT or NON-EXEMPT
# 2 - Calculate the mean, mode, median, and standard deviation of the salaries of each salary grade
# 3 - Calculate the mean, mode, median, and standard deviation of the salaries of EXEMPT employees
# 4 - Calculate the mean, mode, median, and standard deviation of the salaries of NON-EXEMPT employees
# 5 - Create pie charts of the employee status of EXEMPT count by gender and NON-EXEMPT count by gender
# 6 - Create scatter plots of salasry grade by mean salary
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