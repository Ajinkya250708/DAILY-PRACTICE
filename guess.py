import random
number = random.randint(1, 10)
ans="Y"
while ans=="Y":
    user=int(input("Enter a number(1-10):"))
 
    if number==user:
        print("Correct")
        break

    else:
        print("Noo try again")
        
print("computer choosed ", number)