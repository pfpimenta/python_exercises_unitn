"""
2026_04_16

Data Analysis exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.
"""

import pandas as pd

###########################
# step 1 - load data from CSV
filepath = "/home/pfpimenta/python_exercises_unitn/ex2_execution_logs.csv"
df = pd.read_csv(filepath)


###########################
# step 2 - Explore data

### print dataframe preview
print(df)


### How many rows?
print(len(df))

### What are the columns?
print(df.columns)

### What are the column types?
print(df.dtypes)

### Check unique values in each column
for col in df.columns:
    print(f"Column {col}: {df[col].unique()}")


###########################
# step 3 - Extract information from the data

# overall execution_time
print('Average execution time:')
stats = df['execution_time'].mean()
print(stats)

# execution_time per matrix_size
stats = df.groupby('matrix_size')['execution_time'].mean()
print("Execution time per matrix_size:")
print(stats)

# execution_time per num_threads
stats = df.groupby('num_threads')['execution_time'].mean()
print("Execution time per num_threads:")
print(stats)

# execution_time per scheduling_type
stats = df.groupby('scheduling_type')['execution_time'].mean()
print("Execution time per scheduling_type:")
print(stats)


###########################
# step 4 - plot data
import seaborn as sns
import matplotlib.pyplot as plt

# Bar plot - average execution time per configuration (matrix_size)
sns.barplot(data=df, x='matrix_size', y='execution_time')
plt.show()

# Bar plot - average execution time per configuration (num_threads)
sns.barplot(data=df, x='num_threads', y='execution_time')
plt.show()

# Bar plot - average execution time per configuration (scheduling_type)
sns.barplot(data=df, x='scheduling_type', y='execution_time')
plt.show()

# Violin plot - average execution time per configuration (matrix_size)
sns.violinplot(data=df, x='matrix_size', y='execution_time', hue='matrix_size')
plt.show()

# Box plot - average execution time per configuration (matrix_size)
sns.boxplot(data=df, x='matrix_size', y='execution_time')
plt.show()

# Line plot - one line for each matrix_size, with num_threads on the X axis
sns.lineplot(data=df, x='num_threads', y='execution_time', hue='matrix_size')
plt.show()

# Show all 3 params: matrix_size (x), threads (color), and scheduling (columns)
sns.catplot(data=df, x='matrix_size', y='execution_time', hue='num_threads', col='scheduling_type', kind='bar')
plt.show()