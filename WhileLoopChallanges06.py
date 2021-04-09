#WhileLoopChallanges06.py
num = int(input("Enter a number between 10 and 20"))
if num < 10:
    print("Too low")
    print("")
    print("Please try again")
    num = int(input("Enter a number between 10 and 20"))
elif num > 20:
    print("Too high")
    print("")
    print("Please try again")
    num = int(input("Enter a number between 10 and 20"))
elif num > 10 and num < 20:
    print("Thank you")
