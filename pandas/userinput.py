
data = []
total_data = int(input("Enter no of data you want to add here : " ))
for i in range(1, total_data+1):
    print(f"\n Enter details for Employee here {i}")
    
    name = input("Enter Employee name here : ")
    age  = int(input("Enter Employee age here : "))
    designation  =  input("Enter Employee designation  here : ")
    
    
    employee = {
        "Name": name,
        "Age": age,
        "Designation": designation
    }
    
    data.append(employee)
print("\n Final data set ")   
print (f"Employee data set are {data} ")

# pandas strat from here 
import pandas as pd 
df = pd.DataFrame(data)
print("Before info ")
print("\n",df)
print("After info ")
print(df.info())
df.to_csv("Employee.csv", index= True )    