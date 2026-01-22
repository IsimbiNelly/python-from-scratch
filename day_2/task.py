# This is day 2 of learning python from scrath
# Subscripting
print ("Hello"[1])
print (111+222) # Integer = Whole number
print (234_562_345) # Large numbers
print (3.14) # Float = Floating point number
# A function that tells you which data type you are using
print(type("Nelly"))
print(type(1234))
print(type(12.34))
print(type(True))
#Type conversion 
print(int("111")+int("333"))
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
print(3*(3+3)/3-3)
# BMI convert task
height= input("What is your height?")
weight= input("What is your weight?")
BMI= int(weight)/float(height)**2
print(BMI)
print(int(BMI))
print(round(BMI))
print(round(BMI, 4))
# Assignment operator
Score=0
Score+=1
print(Score)
#F-strings
Score = 5
Height = 1.75
print(f"Your score and height is {Score} and your height is {Height}")
#Final project for day 2 (Tip calculator)
print("Welcome to the tip calculator")
bill=input("What was the total bill?")
money=input("How much tip would you like to give? 10, 12 or 15?")
people=input("How many people to split the bill?")
percentage=float(money)/100
potion=1+percentage
tip=(float(bill)/float(people))*float(potion)
print("Your total bill is: " + str(float(bill)))
print("Your percentage tip is: " + str(float(money)))
print("The number of people splitting the bill are: " + str(int(people)))
print("Each person will pay: " + str(round(tip, 2)))
