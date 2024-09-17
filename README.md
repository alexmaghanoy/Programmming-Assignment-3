# Programmming-Assignment-3

## PROBLEM 1: 
- In this problem, we will work with the Pandas Library to load a CSV file into a data frame named `cars.` 
- This CSV file contains information about various car models and their attributes. 
- We are tasked to display the first and last five (5) rows of the provided dataset. 
- Then, the file must be saved as `Surname_Pandas-P1.py.`

### OBJECTIVES:
- Load the data from a CSV file into a Pandas DataFrame named `cars.`
- Display the first five (5) rows of the DataFrame.
- Display the last five (5) rows of the DataFrame.

### CODE PROPER

`import pandas as pd`     
*#import the pandas library*
    
`cars = pd.read_csv('cars.csv')`     
*#load the CSV file into a data frame `cars`*

`cars.head()`     
*#displays the first five (5) rows of the data frame `cars`*

`cars.tail()`     
*#displays the last five (5) rows of the data frame `cars`*

### NOTES:
- The `read.csv` function loads the data from the `cars.csv` file.
- The function `.head()` displays the first five rows, while the function `.tail()` displays the last five rows of the dataset.

### SAMPLE TEST:
Using a sample DataFrame `students`, find and display its first and last three (3) rows:

|      | Surname  | First Name | Age  | Gender    | Program | Year    |
|:----:|:--------:|:----------:|:----:|:---------:|:-------:|:-------:|
|  0   | Diaz     | Samantha   | 21   |  Female   |  ECE    |  4th    | 
|  1   |  Millan  | Cheska     | 18   |  Female   |  EE     |  1st    |
|  2   | Laurez   | Michael    | 19   |  Male     |  CE     |  2nd    |
|  3   | Chua     | Liam       | 20   |  Male     |  IE     |  3rd    |
|  4   | Gonzales | Elaina     | 19   |  Female   |  ME     |  2nd    |
|  5   | Ramos    | Lucas      | 21   |  Male     |  CE     |  4th    |
|  6   | Yves     | Amethyst   | 18   |  Female   |  ECE    |  1st    |

#### EXPECTED OUTPUT:
- **first three (3) rows:**
  
`students.head(3)`
|      | Surname  | First Name | Age  | Gender    | Program | Year    |
|:----:|:--------:|:----------:|:----:|:---------:|:-------:|:-------:|
|  0   | Diaz     | Samantha   | 21   |  Female   |  ECE    |  4th    | 
|  1   |  Millan  | Cheska     | 18   |  Female   |  EE     |  1st    |
|  2   | Laurez   | Michael    | 19   |  Male     |  CE     |  2nd    |

- **last three (3) rows**
  
`students.tail(3)`
|      | Surname  | First Name | Age  | Gender    | Program | Year    |
|:----:|:--------:|:----------:|:----:|:---------:|:-------:|:-------:|
|  4   | Gonzales | Elaina     | 19   |  Female   |  ME     |  2nd    |
|  5   | Ramos    | Lucas      | 21   |  Male     |  CE     |  4th    |
|  6   | Yves     | Amethyst   | 18   |  Female   |  ECE    |  1st    |


## PROBLEM 2:
- In this problem, we will continue using the DataFrame `cars` from the previous Problem 1. 
- Now, we are tasked to extract specific information from this DataFrame through subsetting, slicing, and indexing techniques. 
- Then, the file must be saved as `Surname_Pandas-P2.py.`
  
### OBJECTIVES:
#### a. Subsetting
- Display how many cylinders ('cyl') the car model "Camaro Z28" has.

#### b. Slicing
- Display the row containing the car model "Mazda RX4".
- Display the first five (5) rows of the DataFrame, while showing only the odd-numbered columns (1,3,5,7,9).

#### c. Indexing
- Display the number of cylinders ('cycle) and which gear type ('gear') the car models "Mazda RX4 Wag," "Ford Pantera L," and "Honda Civic" have.

### CODE PROPER

`import pandas as pd`     
*#import the Pandas Library*

`cars = pd.read_csv('cars.csv')`  
*#load the CSV file into a data frame named `cars`*

`Camaro_Z28 = cars.loc[[23],['Model','cyl']]`   
*#**subsetting**: retrieve the number of cylinders for the "Camaro Z28"*

`Mazda_RX4 = cars.loc[cars['Model'] == 'Mazda RX4']`   
*#**slicing**: retrieves the row where "Mazda RX4" is located*

`cars_selected = cars.iloc[0:5, 0:12:2]`   
*#**slicing**: displays the first 5 rows and odd-numbered columns*

`specific_models = cars.loc[[1, 18, 28],['Model', 'cyl', 'gear']]`   
*#**indexing**: retrieves the cylinders and gear type for the given car models//*

### NOTES:
- **Subsetting**: `.loc` function retrieves the number of cylinders ('cyl') for the "Camaro Z28".
- **Slicing**: `.loc` function selects the row where "Mazda RX4" is located. The `.iloc` function displays the first 5 rows and odd-numbered columns.
- **Indexing**: `.loc` function retrieves the "Model", "cyl", and "gear" attributes for specific car models.

### SAMPLE TEST:
By still using the SAMPLE data frame, `students`, extract the following information through subsetting, slicing, and indexing techniques:

|      | Surname  | First Name | Age  | Gender    | Program | Year    |
|:----:|:--------:|:----------:|:----:|:---------:|:-------:|:-------:|
|  0   | Diaz     | Samantha   | 21   |  Female   |  ECE    |  4th    | 
|  1   | Millan   | Cheska     | 18   |  Female   |  EE     |  1st    |
|  2   | Laurez   | Michael    | 19   |  Male     |  CE     |  2nd    |
|  3   | Chua     | Liam       | 20   |  Male     |  IE     |  3rd    |
|  4   | Gonzales | Elaina     | 19   |  Female   |  ME     |  2nd    |
|  5   | Ramos    | Lucas      | 21   |  Male     |  CE     |  4th    |
|  6   | Yves     | Amethyst   | 18   |  Female   |  ECE    |  1st    |
    
1.) Display what program the surname 'Laurez' has.

2.) Display the row that contains the 'Surname' of 'Yves.'

3.) Display the first five (5) rows with odd-numbered columns (1,3,5..) of students.

4.) Display the first name ('first name') and what year ('year') were the students 'Diaz', 'Chua', and 'Gonzales' are.


#### EXPECTED OUTPUT:
- **for number 1:**
  
`Laurez = students.loc[[2],['Surname','Program']]` 
|      | Surname  | Program |
|:----:|:--------:|:-------:|
|  2   | Laurez   |   CE    |

- **for number 2:**
  
`Yves = students.loc[students['Surname'] == 'Yves']`   
|      | Surname  | First Name | Age  | Gender    | Program | Year    |
|:----:|:--------:|:----------:|:----:|:---------:|:-------:|:-------:|
|  6   | Yves     | Amethyst   | 18   |  Female   |  ECE    |  1st    |

- **for number 3:**
  
`students_selected = students.iloc[0:5, 0:6:2]`
|      | Surname  | Age   | Program |
|:----:|:--------:|:------|:-------:|
|  0   | Diaz     |  21   |   ECE   |  
|  1   |  Millan  |  18   |   EE    |  
|  2   | Laurez   |  19   |   CE    |  
|  3   | Chua     |  20   |   IE    | 
|  4   | Gonzales |  19   |   ME    |  

- **for number 4:**
   
`specific_students = students.loc[[0, 3, 4],['Surname', 'First Name', 'Year']]` 
|      | Surname  | First Name |  Year    |
|:----:|:--------:|:----------:|:--------:|
|  0   | Diaz     | Samantha   |   4th    |
|  3   | Chua     | Liam       |   3rd    |
|  4   | Gonzales | Elaina     |   2nd    |

### CONCLUSION:
In this programming assignment, we explored essential data manipulation techniques using the Pandas Library in Python. In `Problem 1`, by loading a CSV file into a DataFrame, we displayed specific portions of the dataset, such as the first and last five rows of it. In `Problem 2`, we performed subsetting, slicing, and indexing operations to extract specific information from the dataset. These skills are essential for performing more effective and precise data analysis for various datasets. 


