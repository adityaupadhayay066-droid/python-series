import pandas as pd
car={
     "Brand": ["Mahindra", "BMW", "Maruti suzuki"],
     "Name": ["Thar", "S1 classic", "Alto 800"],
     "Price": [150000, 500000, 1000000],
     "Type": ["SUV", "Sedan", "Top notch"]
}
df=pd.DataFrame(car)
print("                  Sample Data Frame                       ")
print(df)
print("Single column : Name series:")
print(df['Brand']) #Without using variable 

# printing multicolumn
print("                  \n m_c with Brand and Price                  ")
print("\n column filter  with Brand Mahindra and Price > 150000")
column_filter = df[(df["Brand"] == "Mahindra") & (df["Price"] > 150000)]
print(column_filter)

