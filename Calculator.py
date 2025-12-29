def add(n1,n2):
    return n1 + n2
def sub (n1,n2):
    return n1 - n2
def multiply (n1,n2):
    return n1 * n2
def divide (n1,n2):
     return n1/n2
def cube(n1):
    return n1*n1*n1
print("Select a operation : \n"
      "1.Addition\n"
      "2.Substraction \n"
      "3.Multiply \n"
      "4.Divide \n"
      "5. Cube\n")
s = (input("Select your operation here 1,2,3,4,5 : "))
n1 = int(input("Enter first number here : "))
n2 = int(input("Enter second number here : "))
if (s =="1"):
    print(f"{n1}+{n2} = {n1+n2} ")
elif(s =="2"):
    print (f"{n1}-{n2} = {n1-n2}")  

elif (s =="3"):
    print(f"{n1}X{n2} = {n1*n2}")
elif (s =="4"):
    print(f"{n1}/{n2} = {n1/n2}")
elif(s=="5"):
    print(f"Cube of number is =  { n1*n1*n1} ")
else:
 print("Invalid ❌ try again ")