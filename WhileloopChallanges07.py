num = 10
print("There are",num,"green bottles hanging on the wall")
print(num,"green bottles hanging on the wall")
print ("And if one green bottle should accidentally fall")
num = int(input("How many green bottles would be on the wall"))
if num == 9:
    print("There will be",num,"green bottles hanging on the wall")
elif num != 9:
    print("No try again")
    num = int(input("How many green bottles will be on the wall"))
elif num == 0:
    print("There will be no green bottles on the wall")
