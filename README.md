>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### May 14 2021
Note the the original python project and README file were submitted on August 24. The date given in the heading is the date the original *.py file was copied into the cloned repository.

### Bikeshare

### Description

This project provides some interesting facts about bikesharing in the following cities:

+ Chicago
+ New York City
+ Washington DC

It was created to satisy the project requirements of Udacity's beginner Python data analysis program.

It is a program that works from the command line of any linux-based terminal and uses flags when inputting the city, month and day. Only the city's name is mandatory.

#### Examples

+ python bikeshare.py -c chicago -m may -d wednesday
+ python bikeshare.py -c washington -m february
+ python bikeshare.py -c 'New York City'

### Files used

+ bikeshare.py
+ chicago.csv
+ new_york_city.csv
+ washington.csv

### Credits

I used this website throughout the duration of the project:
[https://pandas.pydata.org/pandas-docs/stable/reference/index.html](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

I used these websites when trying to figure out how best to calculate the most popular journey, which I found to be the most challenging part of the whole exercise:

+ [https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm](https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm)
+ [https://www.geeksforgeeks.org/combine-two-pandas-series-into-a-dataframe/](https://www.geeksforgeeks.org/combine-two-pandas-series-into-a-dataframe/)
+ [https://queirozf.com/entries/pandas-dataframe-groupby-examples#number-of-unique-values-per-group](https://queirozf.com/entries/pandas-dataframe-groupby-examples#number-of-unique-values-per-group)

I also used this specific site to work out how to create a commandline based program:
[https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html)