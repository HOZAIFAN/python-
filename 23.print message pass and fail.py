M=int(input("Enter the marks of student:"))
if(M>=33 and M<=100):
    print("You are passed!")
elif(M<0 or M>100):
    print("you entered invalid marks:")
else:
    print("you are failed:")