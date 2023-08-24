#       Fix Names in a Table

# Table: Users
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

# Problem:
# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.

# The result format is in the following example.
# Example 1:

# Input: 
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+
# Output: 
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

# Solution:
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def fun(name):
        return name.capitalize()

    users['name'] = users['name'].apply(fun)
    return users.sort_values('user_id', ascending=True) 

# or
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def fun(name):
        return name.capitalize()

    users['name'] = np.vectorize(fun)(users['name'])
    return users.sort_values('user_id', ascending=True) 