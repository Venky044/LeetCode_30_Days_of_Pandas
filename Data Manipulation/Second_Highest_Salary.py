#       Second Highest Salary

# Table: Employee
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 
# Problem:
# Write a solution to find the second highest salary from the Employee table. 
# If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.
# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+

# Example 2:
# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+

# Solution:
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates()
    df2 = df.sort_values(ascending=False)
    if len(df2) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})

    Second_Highest_Salary = df2.iloc[1] # 2-1
    return pd.DataFrame({'SecondHighestSalary': [Second_Highest_Salary]})
