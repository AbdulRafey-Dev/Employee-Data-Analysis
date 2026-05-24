# Assigment Bar Chart by Miss Anum
# Tools: Pandas, Matplotlib
# Author: Abdul Rafey



import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman', 'Ayesha', 'Bilal', 'Zara'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 80000, 60000, 90000, 45000, 70000, 85000, 55000],
    'Age': [28, 32, 35, 29, 41, 38, 26, 31],
}

df = pd.DataFrame(data)
print(df)

# Filter 1 - Sirf IT department
it_emp = df[df['Department'] == 'IT']
print("IT Employees:\n", it_emp)


# Filter 2 - Sirf HR department
it_hr = df[df['Department'] == 'HR']
print("HR Employees:\n", it_hr)

# Filter 3 - Salary 60000 se zyada
it_sal = df[df['Salary'] > 60000]
print("High Salaries:\n", it_sal)


# Department wise Average Salary - Bar Chart
dept_salary = df.groupby('Department')['Salary'].mean().reset_index()

plt.barh(dept_salary['Department'], dept_salary['Salary'], color='steelblue')
plt.title('Department wise Average Salary')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.show()


#Department wise Average Age
dept_age = df.groupby('Department')['Age'].mean().reset_index()

plt.bar(dept_age['Department'], dept_age['Age'], color='steelblue')
plt.title('Department wise Average Age')
plt.xlabel('Department')
plt.ylabel('Average Age')
plt.tight_layout()
plt.show()