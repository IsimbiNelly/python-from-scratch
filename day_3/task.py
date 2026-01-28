print ("Welcome to the rollercoaster")
height = int(input("What is your height?"))
if height!=120:
    print("You may proceed :)")
else:
    print("Sorry, you can't proceed because they height doesn't match the requirement :()")
#FIRST TASK OF DAY 3
number = int(input("What is the number you want to check?"))
if number%2 == 0:
    print("Your number is EVEN")
else:
    print("Your number is ODD")
#NESTED IF STATEMENT
print("Welcome to the rollercoaster!")
height= int(input("What is your height?"))
height=120
if height>=120:
    print("You may proceed :)")
    age= int(input("How old are you?"))
    if age<=12:
        print("You will pay $5")
    elif age<=18:
        print("You will pay $10")
    else:
        print("You will pay $15")
else:
    print("You can't proceed because your height doesn't meet the requirement!")
#TSK 2 OF DAY 3 CALCULATING BMI USING IF STATEMENTS
print("Hello there! Let us calculate your BMI.")
height = float(input("What is your height?"))
weight = float(input("What is your weight?"))
bmi = weight / (height ** 2)
print(bmi)
if bmi<18.5:
    print("Based on the calculation, your BMI states you are UNDERWEIGHT!")
elif bmi <25:
    print("Based on the calculation, your BMI states you have NORMAL WEIGHT!")
else:
    print("Based on the calculation, your BMI states you are OVERWEIGHT!")
#TASK 3 OF MULTIPLE IF STATEMENTS TO SUCCESSION
print("Welcome to the rollercoaster!")
height= int(input("What is your height?"))
height=120
bill=0
if height>=120:
    print("You may proceed :)")
    age= int(input("How old are you?"))
    if age<=12:
        bill=5
        print("Kid's ticket is $5")
    elif age<=18:
        bill=10
        print("Teenage's ticket is $10")
    else:
        bill=15
        print("Adult's ticket is $15")
    photo= str(input("Would you like a photo? Type Y for YES or N for NO "))
    if photo=="Y":
        bill+=3
    print(f"Your total is ${bill}")
else:
    print("You can't proceed because your height doesn't meet the requirement!")
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
#LOGICAL OPERATIONS
print("Welcome to the rollercoaster!")
height= int(input("What is your height?"))
height=120
bill=0
if height>=120:
    print("You may proceed :)")
    age= int(input("How old are you?"))
    if age<=12:
        bill=5
        print("Kid's ticket is $5")
    elif age<=18:
        bill=10
        print("Teenage's ticket is $10")
    elif age>=45 and age<=55:
        bill==0
        print(f"You fall under middle age, your bill is ${bill}")
    else:
        bill=15
        print("Adult's ticket is $15")     
    photo= str(input("Would you like a photo? Type Y for YES or N for NO "))
    if photo=="Y":
        bill+=3
    print(f"Your total is ${bill}")
else:
    print("You can't proceed because your height doesn't meet the requirement!")
#FINAL PROJECT FOR DAY 3 TREASURE HUNT!
print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Welcome to JUMANJI!")
print("Your mission is treasure hunting!")

choice = input('You are at the entrance, ' \
'which path do you want to take? ' \
'Type "Left" or "Right" \n').lower()

if choice == "left":
    water = input('You are at the ocean now! ' \
    'Would you like to swim or wait for the boat? ' \
    'Type "Swim" or "Wait" \n').lower()

    if water == "wait":
        boat = input('The boat brought you to the private' \
        ' island, which door do you want to choose? Type "Red",'
        ' "Yellow" or "Blue" \n').lower()

        if boat == "red":
            print("You win! Congratulations! You found the DIAMONDS & GOLD.")
        elif boat == "yellow":
            print("A dragon burnt you! GAME OVER.")
        elif boat == "blue":
            print("Snakes ate you alive! GAME OVER.")
        else:
            print("Invalid door. GAME OVER.")
    elif water == "swim":
        print("You were eaten by sharks! GAME OVER.")
    else:
        print("Invalid choice. GAME OVER.")
elif choice == "right":
    print("GAME OVER.")
else:
    print("Invalid choice. GAME OVER.")
