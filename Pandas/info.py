import pandas as pd
data ={
    "Student_id": [131, 137,146, 123],
    "Name": ["Ritu", "Prasasti", "Aditya", "Random"],
    "City": ["Ghatsila", "Sambhalpur", "Jamshedpur", "Place"]
}
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")


df=pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info()) 
