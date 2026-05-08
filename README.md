# python_exercises_unitn
Exercises made for the Programmazione avanzata ed intelligenza artificiale [146179] class at the University of Trento.


## Install dependencies

Use the tutorials `linux_and_mac_setup_tutorial.md` or `windows_setup_tutorial.md` in this repository to setup.


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
* 1) Load data from a CSV file
* 2) Explore data
    * 2a) How many rows?
    * 2b) What are the columns?
    * 2c) What are the column types?
    * 2d) Check unique values in each column
* 3) Extract information from the data
    * 3a) Overall execution time average
    * 3b) Execution time average per each configuration
* 4) Visualize it in a plot
    * 4a) Bar plot - average execution time

*Bonus*: Find outliers in the data, and generate the plots without them.


## Exercise 3 - Classic ML

*Objective*: Introduction to typical Machine Learning workflow

*Task Description*:
1) Load train data and test data from a CSV file
2) Fit (train) models on the train data: Linear Regression and Decision Tree
3) Evaluate each model on the test data
4) Compare the evaluation results 


## Exercise 4 - Convolutional Neural Networks

*Objective*: Train and evaluate a CNN for an image classification task

*Task Description*:
* 1) Load and visualize the MNIST dataset
* 2) Define the LeNet5 model
* 3) Train
* 4) Evaluate
* extra: compute the confusion matrix and find the most common mistake made by the model (for example: predicts 8s as 3s)
