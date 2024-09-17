### PROGRAMMING ASSIGNMENT 3

## PROBLEM 2

import pandas as pd

# load the data frame, 'cars'
cars = pd.read_csv('cars.csv')
cars

# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars
cars.iloc[0:5, 0:12:2]

# Display the row that contains the ‘Model’ of ‘Mazda RX4’.
Mazda_RX4 = cars.loc[cars['Model'] == 'Mazda RX4']
Mazda_RX4

# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
Camaro_Z28 = cars.loc[[23],['Model','cyl']]
Camaro_Z28

#Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
specific_models = cars.loc[[1, 18, 28],['Model', 'cyl', 'gear']]
specific_models


