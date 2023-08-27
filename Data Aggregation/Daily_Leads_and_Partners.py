#       Daily Leads and Partners

# Table: DailySales
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | date_id     | date    |
# | make_name   | varchar |
# | lead_id     | int     |
# | partner_id  | int     |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
# The name consists of only lowercase English letters.
 
# Problem:
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
# Return the result table in any order.

# The result format is in the following example.
# Example 1:

# Input: 
# DailySales table:
# +-----------+-----------+---------+------------+
# | date_id   | make_name | lead_id | partner_id |
# +-----------+-----------+---------+------------+
# | 2020-12-8 | toyota    | 0       | 1          |
# | 2020-12-8 | toyota    | 1       | 0          |
# | 2020-12-8 | toyota    | 1       | 2          |
# | 2020-12-7 | toyota    | 0       | 2          |
# | 2020-12-7 | toyota    | 0       | 1          |
# | 2020-12-8 | honda     | 1       | 2          |
# | 2020-12-8 | honda     | 2       | 1          |
# | 2020-12-7 | honda     | 0       | 1          |
# | 2020-12-7 | honda     | 1       | 2          |
# | 2020-12-7 | honda     | 2       | 1          |
# +-----------+-----------+---------+------------+
# Output: 
# +-----------+-----------+--------------+-----------------+
# | date_id   | make_name | unique_leads | unique_partners |
# +-----------+-----------+--------------+-----------------+
# | 2020-12-8 | toyota    | 2            | 3               |
# | 2020-12-7 | toyota    | 1            | 2               |
# | 2020-12-8 | honda     | 2            | 2               |
# | 2020-12-7 | honda     | 3            | 2               |
# +-----------+-----------+--------------+-----------------+
# Explanation: 
# For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
# For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].

# Solution:
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['make_name', 'date_id']).nunique().reset_index()
    df.rename(columns={'lead_id':'unique_leads', 'partner_id':'unique_partners'}, inplace=True)
    return df
