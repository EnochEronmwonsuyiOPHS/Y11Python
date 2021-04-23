#Selection005.py
#Enoch
raining = str(input("Is it raining now")).lower()
if raining == "yes":
    windy = str(input("Is it windy today"))
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
            print("take an umbrella")
else:
    print("Enjoy your day")
