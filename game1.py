l = ["stone", "paper", "scissor"]
while(True):
    import random
    z = random.randint(0, 2)
    y = l[z]
    x = input("entre")
    if(x == y):
        print(y)
        print("entre again")
    elif(x == "paper" and y == "stone"):
        print(y)
        print("you win")
    elif(x == "stone" and y == "scissor"):
        print(y)
        print("you win")
    elif(x == "scissor" and y == "paper"):
        print(y)
        print('you win')
    else:
        print(y)
        print("you loose")