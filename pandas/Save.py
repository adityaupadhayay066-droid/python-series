import pandas as pd
data ={
    "Student_id": [131, 137,146, 123],
    "Name": ["Ritu", "Prasasti", "Aditya", "Random"],
    "City": ["Ghatsila", "Sambhalpur", "Jamshedpur", "Place"]
}
df=pd.DataFrame(data)
print(df)
# df.to_excel("Friends.xlsx",index=False) # index=False mean it will remove indexing ( 0,1,2...)
df.to_csv("Data.csv", index=False)

