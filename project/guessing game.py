import random 
Cnumber=random .randrange(1,101)
userInput=int(input ("Enter your numbr-----"))
if userInput>Cnumber:
    print("computer Number",Cnumber)
    print("your guess number is high")
elif Cnumber>userInput:
    print("your  guess number is too low")
    print("computer Number",Cnumber)
else:
    print("your guess number is equal")
    print("computer Number",Cnumber)



