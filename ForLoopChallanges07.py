#ForLoopChallanges07.py
total = 0
for i in range(0,4):
    num1 = int(input("Enter a number"))
    q = str(input("Do you want that number to be included y or n"))
    if q == "y":
        total = total + num1
    elif q == "n":
        print("We will move on then")
print("The total is", total)    
