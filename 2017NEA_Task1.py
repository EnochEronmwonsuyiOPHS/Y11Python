#Creating subprogram
def registration():
    # Obtaining detail of player
    print("League Registration")
    firstname = str(input("Enter your first name"))
    lastname = str(input("Enter your last name"))
    nickname = str(input("Enter your nickname"))
    emailaddress = str(input("Enter your email address"))
    skilllevel = str(input("Enter a skill level E for expert or C for casual"))
    #Reviewing details
    print("Please review your details")
    print("Your firstname is", firstname)
    print("Your lastname is", lastname)
    print("Your nickname is", nickname)
    print("Your email is", emailaddress)
    if skilllevel == "E":
        print("Skill level is Expert")
    elif skilllevel == "C":
        print("Skill level is Casual")
        
    #Asking if details are correct
    
    q = str(input("Are these details correct y or n"))
    if q == "y":
        print("You have been registered")
    if q == "n":
        registration()
        
registration()        
        
