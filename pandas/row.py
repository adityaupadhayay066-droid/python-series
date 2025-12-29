# head(n) if i provide n it will pass first n row of data if i dont give n it will pass first 5 row of data 
# tail (n) it will pass last row of data (If i not provide n it work same as head(n))
import pandas as pd 
df=pd.read_excel("Book1.xlsx")
print("-----------First 2 row of ---------------")
# print(df.head(2)) # it wil display frst 2 row 
print(df.head()) # it will pass first 5 row of data 
print("--------Last 5 row---------------  ")
# print(df.tail(5))
print(df.tail()) # it will pass last 5 row of data  
