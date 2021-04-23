#WhileLoopChallanges05.py
#Enoch
compnum = 50
guess = int(input("Guess the competition number"))
count = 1
while guess != compnum:
    if guess < compnum:
        print("You guess was too low")
        guess = int(input("Guess the competition number"))
        count = count + 1
        
    if guess > compnum:
        print("Your guess was too high")
        guess = int(input("Guess the competition number"))
        count = count + 1
    
    if guess == compnum:
        print("Well done you guessed the number")
