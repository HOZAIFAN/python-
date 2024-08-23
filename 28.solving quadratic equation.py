a=float(input("Enter first cofficent a:"))
b=float(input("Enter second cofficent b :"))
c=float(input("Enter thirdS cofficent c:"))
disc=b*b-4*a*c
import math
if(disc>0):
    print("it have two real solution:")
    print("first real solution",(-b+math.sqrt(disc))/(2*a))
    print("second real solution",(-b-math.sqrt(disc))/(2*a))
elif(disc==0):   
    print("There is only one real solution",-b/(2*a))
else:
    print("There is no real solution")