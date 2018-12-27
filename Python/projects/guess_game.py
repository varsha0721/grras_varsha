import random
a = random.randint(1,50)
while input("\n\n press any key to contineue:"):
 i=0
 while i <= 5:
    b=int(input("guess the no:"))
    if a == b:
        print(a);print(b)
        print("you won")
        break
    elif a < b:
        print("enter small no")
    elif b < a:
        print("enter a big no")
    elif(i==5):
        print("you loose")
        
    i=i+1

