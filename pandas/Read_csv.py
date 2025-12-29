import pandas as pd 
df =pd.read_csv("sales_data_sample.csv", encoding="latin1")
df=pd.read_excel("SampleSuperstore.xlsx")
df=pd.read_excel('Book1.xlsx')
print(df)
