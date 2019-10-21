
import random

last = "" #so that they can hit any key and it will do the last one

while True:
    dice = random.randint(1,6) #dice role generator
    coin = random.randint(1,2) #coin toss generator

    user = input("coin toss (c) dice role (d) quit") #asking if the user wants a dice role or a coin toss
    
    if   user.lower() == "c": #if they want a coin toss
        last = "c"
        print(coin)

    elif user.lower() == "d": #if they want a dice role
        last = "d"
        print(dice)

    elif user.lower() == "quit":
        print("goodbye")
        break

    else: # if first time will make them try again when given a bad input
          # otherwise will make the last choice
        if last == "": # invalid input for the first cycle
            print("sorry try again")

        elif last == "c": #if they want a coin toss
            print(coin)

        elif last == "d": #if they want a dice role
            print(dice)
        