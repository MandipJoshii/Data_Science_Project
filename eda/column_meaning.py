# NOTE:

## 1. IN SCHOOL ROW:

#### GP = Gabriel Pereira
#### MS = Mousinho da Silveira

## 2. IN ADDRESS ROW:

#### U = URBAN
#### R = RURAL

## 3. FAMILY SIZE(FAMSIZE)

#### LE3 -> LESS THAN OR EQUAL TO 3
#### GT3 -> GREATER THAN 3 

## 4. PSTATUS

#### T = TOGETHER
#### A = APART

## 5. FAMREL -> FAMILY RELATIONSHIP QUALITY

## 6. FREE TIME = STUDENT FREE TIME AFTER SCHOOL

## 7. DALC = WORKDAY ALCOHOL CONSUMPTION

## 8. WALC = WEEKEND ALCOHOL CONSUMPTION

## 9. G1 = FIRST EXAM RESULT, G2 = SECOND EXAM RESULT, G3 = FINAL EXAM RESULT

##### THE COUNT() IS USED TO IGNORE NULL VALUE AND COUNT ALL NON-NULL VALUE
##### THE DROPNO() IS USED TO REMOVE ALL THE NLL VALUE 

### MAIN GOAT -> CHECKING MISSING VALUE(MEAN,MEDIAN, MOST_FREQUENT), 

import pandas as py
import matplotlib.pyplot as plt

df = py.read_csv("student-mat.csv", delimiter=";")



#1. how big is the data
print(df.shape)

#2 how does the data looks like?
print(df.head())
print(df.sample(5))

#3. number of column dataype
print(df.info())

#4. are there any missing value
print(df.isnull().sum())

#5. how does the data looks mathemetically
print(df.describe())

#6. are there any duplicate value
print("duplicated value: ", df.duplicated().sum())


# print(df.head())
# print(df.columns)
# print(df.describe())

import pandas as py
import matplotlib.pyplot as plt

df = py.read_csv("student-mat.csv", delimiter=";")

plt.scatter(df["Fedu"], df["G3"], color='blue', label='G3 vs Father Education')
plt.scatter(df["Medu"], df["G3"], color='green', label='G3 vs Mother Education')
plt.title("Final Grade vs Parents' Education")
plt.xlabel("Education Level")
plt.ylabel("Final Grade (G3)")
plt.grid(True)
plt.legend()
plt.show()
