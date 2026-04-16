# python_exercises_unitn
Exercises made for the Programmazione avanzata ed intelligenza artificiale [146179] class at the University of Trento.

## Exercise 1 - Fibonacci

*Objective*:
Get everyone's environment running and demonstrate Python’s simplicity.

*Task Description*: 
Write a Python script that calculates and prints the terms of the Fibonacci sequence up to a term N defined by the user via the terminal.

The sequence is defined by the recurrence relation:
```
    F(1) = 0
    F(2) = 1
    F(n) = F(n-1) + F(n-2)
```

*Bonus*: Write the sequence to a file named fibonacci.txt.


## Exercise 2 - Data Analysis
*Objective*: Get introduced to Python's most popular data analysis tools and workflow

*Task Description*:
1) Load data from a CSV file
2) Explore data
    2a) How many rows?
    2b) What are the columns?
    2c) What are the column types?
    2d) Check unique values in each column
3) Extract information from the data
    3a) Overall execution time average
    3a) Execution time average per each configuration
4) Visualize it in a plot
    4a) Bar plot - average execution time

*Bonus*: Find outliers in the data, and generate the plots without them.


### Install dependencies

First, create a virtual environment:
```bash
python3 -m venv venv_python_unitn
```

Then, activate it:
```bash
source venv_python_unitn/bin/activate
```

Then install dependencies:
```bash
pip install pandas numpy seaborn
```

Test if the dependencies are correctly installed:
```bash
python3
import numpy
import pandas
import seaborn
```
