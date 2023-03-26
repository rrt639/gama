import random
a= int(input("enter number:"))
b= random.randint(0,9)
if a>b:
    print ("you won")
elif a==b:
    print ("draw")
else:
    print("you're loseeer")
