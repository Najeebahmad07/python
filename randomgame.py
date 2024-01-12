import random
a=random.randrange(1,100)
b=int(input("Enter Number"))
if a>b:
    print("Computer Number Is",a)
    print("your number is Low")
elif a>b:
    print("Your Number Is high")
else:
    print("Number is equal")