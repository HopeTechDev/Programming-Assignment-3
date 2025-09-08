# Programming-Assignment-3
Advanced Programming - Python Data Analysis

**Author:** SAEZ, Eljenzal Hoper U.  
**Course:** Advanced Computer Programming and Algorithms / ECE2112

---

## 📌 Description
This programming exercise is designed to develop proficiency in data manipulation using the Python programming language and the pandas library within a Jupyter Notebook environment. The task involves loading a car dataset from a CSV file, performing exploratory data analysis, and extracting specific information through subsetting, slicing, and indexing techniques.

---

## ⚙️ Requirements
- Python 3.x  
- Jupyter Notebook
- Install pandas if not already installed.
- Download the required CSV (bit.ly/Cars_file)

---

## ▶️ How to Run
1. Save the CSV in your default user folder
2. Open a terminal or command prompt
3. Navigate to the folder with your .py files
4. Run the scripts using:
   - *python SAEZ_Pandas-P1.py*
   - *python SAEZ_Pandas-P2.py*

---

## 💡 Examples w/ Explanation

### 01 🧠 Problem 1

```python

#a. Load the corresponding .csv file into a data frame named cars using pandas
#b. Display the first five and last five rows of the resulting cars.
import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas
p1 = pd.concat([cars.head(), cars.tail()]) #display the first 5 rows and last 5 rows of cars.csv
p1

```

#### Code Explanation:

- cars = pd.read_csv("cars.csv") → loads the dataset cars.csv into a Pandas DataFrame named cars.
- cars.head() → returns the first 5 rows of the dataset.
- cars.tail() → returns the last 5 rows of the dataset.
- pd.concat([...]) → combines both sets of rows into a single DataFrame.
- The result is stored in a new DataFrame called p1


### 02 🧮 Problem 2

```python

import pandas as pd  # Import the pandas library
cars = pd.read_csv("cars.csv")  # Load the .csv file into a DataFrame named cars

```
 dataset cars.csv → read and stored in a DataFrame called cars.

```python

cars.iloc[:, ::2].head()

```
- .iloc[:, ::2] → selects all rows (:) but only every 2nd column starting from the first one (::2).
- .head() → shows the first 5 rows of those selected columns.
  

```python

cars.loc[cars['Model'] == 'Mazda RX4']

```
- .loc[...] →  used to filter rows.

- This returns the rows where the Model column is exactly 'Mazda RX4'.
  

```python

cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

```
- Filters the DataFrame for rows where Model = 'Camaro Z28'.

- Returns only the Model and cyl (cylinders) columns.

```python

models = (...)

```
- Creates a tuple containing the car models you want to filter.

```python

cars['Model'].isin(models)

```

- Checks if each row’s Model is one of the values in the tuple.

- Returns True for matching rows, False otherwise.


```python


cars.loc[..., ['Model','cyl','gear']]

```

- .loc[...] → selects the rows where the condition is True.

- ['Model','cyl','gear'] → specifies which columns to return.


---

##### *- 🌱 "The future belongs to those who believe in the beauty of their dreams."*

---

### 📝 Commitments
- **v1.0** – Initial draft  
  - Loaded CSV file into pandas DataFrame
  - Displayed first and last 5 rows
  - Basic checks with print statements

- **v1.1** – Data Loading
  - Applied slicing and indexing for specific queries

- **v1.2** – Final Touches 
  - Cleaned up variable names and comments
  - Improved formatting for readability
  - Final review of code and README layout














