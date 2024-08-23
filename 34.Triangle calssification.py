#here L1 L2 L3 represents lenght of three sides of triangle
L1=float(input("Enter the length of first side of trangle:"))
L2=float(input("Enter the length of first side of trangle:"))
L3=float(input("Enter the length of first side of trangle:"))
if(L1!=0 and L2!=0 and L3!=0):
    if(L1==L2 and L2==L3 and L3==L1):
        print("The traingle is equiliteral.")
    elif(L1==L2 or L2==L3 or L3==L1):
        print("The traingle is isoceles.") 
    else:
        print("The triangle is scalene.")
else:
        print("You entered one side of triangle zero,hence triangle is not possible.")