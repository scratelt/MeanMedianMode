# Challenge: Mean, Median, and Mode

The challenge is to use everything you have learned so far to write a full module that is reusable both as a package and as a direct monolithic python script that can calculate the mean, median, and mode of a data set of numbers.

---

## Challenge Data Sets

You will use these data sets as the sample data to pass through your functions as this covers a lot of the edge cases you can expect.

data_set_one = [6, 9, 1, 2, 6, 3, 7]
data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]
data_set_four = [6, 9, 1, 2, 3, 7, 4, 8]

---

## Overview & Acceptance Criteria

1. Mean:

  + Average of a data set

  + Get the sum of all the numbers & divide by however many numbers there are

  + I want the average rounded to three decimal places


2. Median:

  + Middle number in a data set

  + Get the middle number in a data set that is ordered by value and if the length of the data set is even, then you give me the average of the two middle numbers

  + I want the median rounded to two decimal places


3. Mode:

  + Most common number in a data set

  + Get the number that has the highest frequency in the data set, there can be multiple (there can also be no mode)

  + I want the mode returned as a list

---

## Module Structure

The structure of the application should be as follows:

calc_mean funtion
  takes in a dataset
  returns the mean

calc_median funtion
  takes in a dataset
  returns the median

calc_mode function
  takes in a dataset
  returns the mode

solve_dataset function
  takes in a dataset
  returns mean, median, and mode

main function
  hard codes all datasets
  prints mean, median, and mode for each data set

---

## Styling & Documentation

Your application should have a module docstring

All functions should have a detailed docstring that describes what it does with annotations in the signatures and should conform to google style docstrings

Print statements with mean, median, and mode should be descriptive and not just numbers
