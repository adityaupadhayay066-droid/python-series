import pandas as pd
car={
     "Brand": ["Mahindra", "BMW", "Maruti suzuki","Ferrari", "Lamborgini"],
     "Name": ["Thar", "S1 classic", "Alto 800","296 GTB","Revelto"],
     "Age": [18,18,16,30,25],
     "Price": [150000, 500000, 1000000, 10000000,20000000],
     "Type": ["SUV", "Sedan", "Top notch","V6 Electric", "Hybrid"]
}
df =pd.DataFrame(car)
print("  Car with price> 15 Lakh      ")
print(df[df["Price"]>150000])  # filtering single row  using single condition


#  filtering row age>19 & price > 50 Lakh
row =df[(df["Age"]>19) & (df["Price"]> 500000)]   #df[(condition1) & (condition2)]   ✅

print("----------------- Car  price > 50 Lakh & age>19 --------------- ")
print("\n",row)     


# Using OR)(|) condition
print("\n")
print("-----------      Car brand using OR operator        \n ------------------------------------")
filtered_or= df[(df["Age"]>16) | (df["Price"]>1500000)]
print(f"Car brand with price > 15 lakh OR Driver age > 16 \n:  {filtered_or}")
