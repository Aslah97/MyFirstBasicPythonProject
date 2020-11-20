print("\t\t\t +++ My First Basic Python Project +++   ")
print("\n")
# Initialize variables
health = 10

#  User inputs: 
name = str(input("Enter your name: "))
if name.isdigit():
    print("Invalid entry! Your name cannot be a number")
else:
    print("Welcome to the game,",name.upper(),"!")

# Verifying the age:
age = int(input("Enter your age: "))
if age<13 :
    print("You've to be 13 or older to play....")
    exit()

# Requesting permission:
answer = input("Do you want to play? (Yes/No) ").lower()
if answer == "yes" :
    print("Great! Let's play! ")
    print("You start with", health,"health")
elif answer == "no":
    print("See you next time!")
else:
    print("Invalid entry!")

# Choices:
choice1 = input("Do you want to drive or swim? (drive/swim) ").lower()
if choice1 == "drive" :
    print("You got hit by another car & you lost 5 health!")
    health -= 5
    choice3 = input("Do you want to go to the hospital? (Yes/No) " ).lower()
    if choice3 == "yes" :
        print("You win!")
    else :
        print("You lose!")

elif choice1 == "swim" :
    choice2 = input("You swam across the river and found a house. Do you want to enter the house? (Yes/No) ").lower()
    if choice2 == "yes":
        print("You win!")
    else :
        print("You lose!")

else:
    print("Invalid input!")

