import random
computer = random.randint(0,2)
player = int(input("stein(0), schere(1), papier(2)" ))
if 0 <= player <= 2:
    if (((player == 0) and (computer == 1)) or
        ((player == 1) and (computer == 2)) or
        ((player == 2) and (computer == 0))):
        print("win")
    elif player == computer:
        print("tie")
    else:
        print("lose")