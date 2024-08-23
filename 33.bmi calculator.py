weight=float(input("Enter your weight"))
height=float(input("Enter your height"))

BMI = weight / (height**2) #body mass index

if(BMI<18.5 and BMI>0):   
    print("Underweight","Your BMI is",BMI)
elif(BMI>=18.5 and BMI<=25):
    print("Normal weight","Your BMI is",BMI)
elif(BMI> 25 and BMI< 30):
    print("Overweight","Your BMI is",BMI)
elif( BMI>=30):
    print("Obese","Your BMI is",BMI)
else:
    print("invalid ","Your BMI is",BMI)
