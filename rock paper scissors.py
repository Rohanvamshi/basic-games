
import random
run = True
while run:
    user = input(' play! enter your choice       ')
    computer = random.choice([0,1,2])

    if user== "Rock" or user == 'rock':
        if computer == 0:
            print("Draw!!")
        if computer == 1:
            print("AI Wins!")
        if computer == 2:
            print("you saved humanity")
    elif user == "Paper" or user == "paper":
        if computer == 0:
             print("you saved humanity")
        if computer == 1:
            print("Draw!!")
        if computer == 2:
            print("AI Wins!")
    elif user == "scissors" or user == "Scissors":
        if computer == 0:
             print("AI Wins!")
        if computer == 1:
            print("you saved humanity")
        if computer == 2:
            print("Draw!!")

    else:
        print("no typos! humanity is in your hands!! ")

    user2 = input("do you want to continue? y or n       ")
    if user2=='n':
        run =False
        print(" good game!  ")
