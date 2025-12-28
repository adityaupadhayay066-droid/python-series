import random
computer_number= random.randint(1,18)
user_number=int(input(" 🎯 Enter the number between 1 to 18 here: "))

if (computer_number==user_number):
    print("🎉 Congratulations! You guessed the correct number!")
else:
    print("Wrong guess")
    print(f"🖥️ Computer number was :{computer_number}")

