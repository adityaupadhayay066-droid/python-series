# adding column

import pandas as pd

data ={
       "Brand": ["Mahindra", "BMW", "Maruti suzuki"],
     "Name": ["Thar", "S1 classic", "Alto 800"],
     "Price": [150000, 500000, 1000000],
     "Type": ["SUV", "Sedan", "Top notch"]
}
df = pd.DataFrame(data)
print(df)

""" 
# Adding new column in data 
           "syntax"
df["Column name ] = some data 

        syntax using insert method 
df.insert(loc,"Column name", some_data)

no of row = no of column 

"""
df["Manufacture_year"]=[2022 ,2018, 2016]
print(df)

# using insert method 
print("     \n    Add Manufacturing year using insert method       ")

df.insert(1, "Manufacturing year", [2022 ,2018, 2016])
print(df)
