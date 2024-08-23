age=int(input("Enter your age:"))
if(age>18):
    print("You can vote\nyou can also make your license")
elif(age>0 and age<=18):
    print("you are not eligible for anything")
else:
    print("Enter valid age")