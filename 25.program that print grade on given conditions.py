M=int(input("Enter marks of student:"))
if(M<=100 and M>=90):
    print("SUPERB 'A' grade.")
elif(M<90 and M>=80):
    print("EXCELLENT 'B' grade.")
elif(M<80 and M>=70):
    print("GOOD  'C' grade.")
elif(M<70 and M>=60):
    print("you are passed.")
elif(M<60 and M>0):
    print("you ar failed.")
else:
    print("you entered invalid marks.")