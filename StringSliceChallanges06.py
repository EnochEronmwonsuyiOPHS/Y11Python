#StringSliceChallanges06.py
#Enoch
firstname = str(input("Enter your first name"))

if len(firstname) < 5:
    lastname = str(input("Enter your last name"))
    fullname = firstname + lastname
    caps = firstname.upper()
    print(caps)

else:
    print(firstname.lower())
