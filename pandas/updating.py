import pandas as pd

data ={
          "Brand": ["Mahindra", "BMW", "Maruti suzuki","Ferrari", "Lamborghini"],
     "Name": ["Thar", "S1 classic", "Alto 800","296 GTB","Revelto"],
     "Age": [18,18,16,30,25],
     "Price": [150000, 500000, 1000000, 10000000,20000000],
     "Type": ["SUV", "Sedan", "Top notch","V6 Electric", "Hybrid"]
}
df =pd.DataFrame(data)
# df.loc[df["Name"].isin(["Fortuner", "Mercedes"]),"Price"]= 55000000
df.loc[0,"Price"]=550000
print(df,"\n")

print("             Unique value in name column           ")
print(df["Name"].unique())  # it find the distinct value and remove duplicate
