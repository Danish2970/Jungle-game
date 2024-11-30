heading="Welcome To Jungle game"
print(heading)
title="A man want to go out from the jungle without any trouble so you will help the man to got out from the jungle with the help of game"
print(title)
a=int(input("press 1 for the left and press 2 for the right "))
if a==1:
    print("Reached at another Point ")
    z=int(input("press 1 for left turn OR press 2 for right turn from the point"))
    if z==1:
        print("game over : you have reached the dead end")
    elif z==2:
        print("game over: you have reached to the bear cave ")
elif a==2:
    print("reached near village ")
    x=int(input("Press a for left OR press 2 for right turn"))
    if x==1:
        print("woohoo : you met with stranger (man)")
        y=int(input("press 1 for taking help from the stranger OR press 2 for ignore the stranger"))
        if y==1:
            print("congratulations you have safely reached the town ")
        elif y==2:
            print("you loose :reached near waterfall ")
    elif x==2:
        print("Game over : reached in front of tiger ")