n=float(input("Enter a number between 1 and 10:"))
if(n>=10):
    print("The square of number is:",n*n)
elif(n>0 and n<10):
    print("The cube of number is:",n*n*n)
else:
    print("Your entered invalid number.")