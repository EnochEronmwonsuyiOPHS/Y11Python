 #StringSliceChallanges04.py
 firstline = str(input("Enter the first line of a nursery rhyme"))

length = len(firstline)

print("This has", length, "letters in it")

startnum = int(input("Enter a starting number"))
endnum = int(input("Enetr an ending number"))

part = firstline[startnum : endnum]
 
print(part)
