#!/usr/bin/python3


def exo6():
    response = int(input("Please enter your number: "))
    while response < 10 and response < 20:
        print("ok")
        if response < 10:
            print("« Plus petit ! »")
        elif response > 20:
            print("« Plus grand ! »")


#exo6()

def exo10():
    age = int(input("Please enter your age: "))
    if  age <= 6 and age <7:
        print("you are a poussin")
    elif age <= 8 or age < 9:
        print("you are a Pupille")
    elif age <= 10 or age < 11:
        print("you are a Minime")
    elif age > 12:
            print("you are a poussin")
#exo10()
