#ForLoopChallanges08.py
q = str(input("Do you want to count up or down, u or d"))

if q == "u":
    topnumber = int(input("Enter the top number"))
    for i in range(1,topnumber,+1):
        print(i)

elif q == "d":
    downnumber = int(input("Enter a number below 20"))
    for i in range(20,downnumber,-1):
        print(i)
else:
    print("I don't understand")
