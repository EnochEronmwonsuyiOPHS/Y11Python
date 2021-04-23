#2017NEA_Task2.py
#Enoch
#Creating subprogram
def fee_calc():
    print("Welcome to the fee calculator")
    #Gathering details
    
    email_address = str(input("Enter your email address"))
    skill_level = str(input("Enter your skill level E for expert or C for casual"))
    country = str(input("Where do u live, UK, US or AU"))
    
    #Adding extra money depending on skill level
    entryfee = (10)
    if skill_level == "E":
        entryfee = entryfee + 35
    elif skill_level == "C":
        entryfee = entryfee + 20
    
    #Converting between currancy    
    if country == "UK":
        print("The entry fee is", entryfee,"GBP")
    elif country == "US":
        print("The entry fee is", entryfee * 1.5, "USD")
    elif country == "AU":
        print("The entry fee is", entryfee * 2, "AUD")
    
    #Asking if user wants to calculate another fee
    q = str(input("Do you want to calculate another fee Y or N"))
    if q == "Y":
        fee_calc()
        
    elif q == "N":
        print("Thank you your fee had been successfully calculated")

#Casting subprogram        
fee_calc()


#I started by creating a subprogram to calculate the fee.

#I display fee calculator and then gather the details by casting variables.

#Then I added the bonus money to the fee by using if statements depending on whther or not the player was expert or casual.

#Then I converted the entry fee into the appropriate currancy depending on the country the user was from.

#After I asked whether or not the user wanted to calculate another fee.

#If they do I call the subprogram and if they don't I print a thank you message.

#After finishing the subprogram I call it to allow the user to begin with the fee calculator. 
