#print ("Welcome to the rollercoaster")
#height = int(input("What is your height?"))
#if height!=120:
#    print("You may proceed :)")
#else:
#    print("Sorry, you can't proceed because they height doesn't match the requirement :()")
#FIRST TASK OF DAY 3
#number = int(input("What is the number you want to check?"))
#if number%2 == 0:
#    print("Your number is EVEN")
#else:
#    print("Your number is ODD")
#NESTED IF STATEMENT
#print("Welcome to the rollercoaster!")
#height= int(input("What is your height?"))
#height=120
#if height>=120:
#    print("You may proceed :)")
#    age= int(input("How old are you?"))
#    if age<=12:
#        print("You will pay $5")
#    elif age<=18:
#        print("You will pay $10")
#    else:
#        print("You will pay $15")
#else:
#    print("You can't proceed because your height doesn't meet the requirement!")
#TSK 2 OF DAY 3 CALCULATING BMI USING IF STATEMENTS
#print("Hello there! Let us calculate your BMI.")
#height = float(input("What is your height?"))
#weight = float(input("What is your weight?"))
#bmi = weight / (height ** 2)
#print(bmi)
#if bmi<18.5:
#    print("Based on the calculation, your BMI states you are UNDERWEIGHT!")
#elif bmi <25:
#    print("Based on the calculation, your BMI states you have NORMAL WEIGHT!")
#else:
#    print("Based on the calculation, your BMI states you are OVERWEIGHT!")
#TASK 3 OF MULTIPLE IF STATEMENTS TO SUCCESSION
#print("Welcome to the rollercoaster!")
#height= int(input("What is your height?"))
#height=120
#bill=0
#if height>=120:
#    print("You may proceed :)")
#    age= int(input("How old are you?"))
#    if age<=12:
#        bill=5
#        print("Kid's ticket is $5")
#    elif age<=18:
#        bill=10
#        print("Teenage's ticket is $10")
#    else:
#        bill=15
#        print("Adult's ticket is $15")
#    photo= str(input("Would you like a photo? Type Y for YES or N for NO "))
#    if photo=="Y":
#        bill+=3
#    print(f"Your total is ${bill}")
#else:
#    print("You can't proceed because your height doesn't meet the requirement!")
#TASK 4 PIZZA DELIVERY
print("Welcome to Python Pizza Deliveries")
size= str(input("What size of pizza do you want? S, M or L"))
pepperoni= str(input("Do you want pepperoni on your pizza? Y or N"))
extra_cheese= str(input("Do you want extra cheese on your pizza? Y or N"))
bill=0
if size=="S":
    bill+=15
elif size== "M":
    bill+=20
else:
    bill+=25
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
        bill+=1
        print(f"Your total bill is ${bill}")
else:
     print(f"Your total bill is ${bill}")