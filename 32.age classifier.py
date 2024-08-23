age=float(input("Enter the age of child:"))
if(age<=0):
    print("He is not born yet")
if(age>0 and age<=12):
    print("He is a child")
elif(age>12 and age<=19):
    print("He is a teenage")
elif(age>19 and age<=64):
    print("He is a adult")
else:
    print("He is senior") 