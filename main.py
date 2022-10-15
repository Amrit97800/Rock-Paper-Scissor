import random


def Win(comp, user):
    if comp == user:
        print("\tIts tie!")
    

    elif user!="R" and user!="P" and user!="S":
        print("Wrong input : Choose Rock(r), Paper(p), Scissor(s)")
    
    elif comp == "R":
        if user == "P":
            print('\tYou win!')
        elif user == "S":
            print("\tYou loose!")
            
    elif comp == "P":
        if user == "S":
            print('\tYou win!')
        elif user == "R":
            print("\tYou loose!")

    elif comp == "S":
        if user == "R":
            print('\tYou win!')
        elif user == "P":
            print("\tYou loose!")

while True:
    comp = 0

    ch = random.randint(1, 3)
    if ch == 1:
        comp = "R"
    elif ch == 2:
        comp = "P"
    elif ch == 3:
        comp = "S"

    # print(comp)

    user = input("Rock(r), Paper(p), Scissor(s) : ")
    user=user.capitalize()

    if user=="Q":
        break


    Win(comp, user)


print("Thanks for playing!")
