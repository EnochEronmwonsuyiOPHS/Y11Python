#WhileLoopChallanges04.py
count = 0
while count < 5:
    guest1 = str(input("Enter the name of guest"))
    print(guest1, "has now been invited to the party")
    count = count + 1
    q = str(input("Do you want to invite more people y or n"))
    if q == "y":
        guest2 = str(input("Enter the name of guest"))
        print(guest2, "has now been invited to the party")
        count = count + 1
    if q == "n":
        print(count, "guests have been invited")
