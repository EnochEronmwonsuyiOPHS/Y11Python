#WhileLoopChallanges03.py
#Enoch
num = int(input("Enter a number"))
firstnum = num
total = firstnum
looping = "y"

while num < 50:
    num2 = int(input("Enter another number"))
    total = firstnum + num2
    question = str(input("Do you want to add another    number y or n"))
    if question == "y":
        num3 = int(input("Enter a number"))
        total = total ++ num3
    if question == "n":
        print("The total is",total)
