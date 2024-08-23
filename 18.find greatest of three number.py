a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter  third number:"))
if(a>b and a>c):
    print("The greater number is first:",a)
elif(b>a and b>c):
    print("The greater number is second:",b)
else:
    print("The greater number is third:",c)