#ForLoopChallanges09.py
num = int(input("How many people are you inviting to the party"))

if num < 10:
    for i in range(0,num):
        nameofguest = str(input("What is the name of the guest"))
        print(nameofguest, "has been invited")
        
if num >= 10:
    print("Too many people")
