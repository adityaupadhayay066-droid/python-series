def bmi_calculator():
    print("---------------------")
    print("  BMI calculator ")
    print("---------------------")
    weight = float(input("Enter weight in Kg here : "))
    height_feet = float(input("Enter height in feet here : "))
    height_m = height_feet *0.3048
    bmi = weight/(height_m**2)
    bmi = round(bmi,2)
    print(f"BMI is {bmi}")
    if ( bmi < 18.5):
        print("Underweight")
    elif (bmi < 25):
        print("Normal Weight")
    elif (bmi < 30):
        print("OverWeight")
    else:
        print("Obese")

    print("Thank You 👍")
  
bmi_calculator()
