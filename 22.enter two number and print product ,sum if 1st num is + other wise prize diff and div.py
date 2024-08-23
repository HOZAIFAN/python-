n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if(n1>0):
    print("The sum of two number is :",n1+n2)
    print("The product of two number is:",n1*n2)
elif(n1<0):
    print("The diff of two number is :",n1-n2)
    print("The div of two number is:",n1/n2)
else:
    print("The first number is zero:")