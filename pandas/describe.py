import pandas as pd
data = {
    "StudentID":  [18,54,56],
    "Name": ["Alice", "Johnson","Charlie"],
    "Subject": ["Maths", "Computer Science", "Physics"]

}
df=pd.DataFrame(data)
print("--------------Sample data frame------------")
print(df)
print("xxxxxxx/ Describe data /xxxxxxxxx ")
print(df.describe())
