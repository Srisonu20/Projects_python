# import random
# x = random.randint(1,10)
# y = int(input("enter"))
# if x ==y:
#     print("YOU WON")
# else:
#     print("You Lost")




# secret_number = random.randint(1, 10)
# user_number = int(input("Guess a number = "))
#
# # IF-ELSE
# if user_number == secret_number:
#     print("You won")
# else:
#     print(f"You lost, the number was {secret_number}")


# import  random
#
# list = ["r","p","s"]
# com = random.choice(list)
#
# user = input("eneter")
#
# if user  in "r":
#     print("won")
# elif user == "p":
#     print("no")
# else:
#     print("over")

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
user_choice = input("Enter your guess [rock/paper/scissors] = ").lower()
# Converts to lowercase
# ROCk -> rock

# IF-ELIF-ELSE
if user_choice != "paper" and user_choice != "rock" and user_choice != "scissors":
    print("Invalid choice")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You won")
elif user_choice == computer_choice:
    print("Tied")
else:
    print(f"You lost, the computer choice was {computer_choice}")