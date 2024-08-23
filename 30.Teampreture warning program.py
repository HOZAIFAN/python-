T=float(input("Enter tampreature:"))
if(T<0 and T>-50):
    print("Teampreature is too  much cold outside")
elif(T>=0 and T<=25):
    print("Teampreture is cold")
elif(T>25 and T<=40):
    print("Teampreature is hot out side and light uv radiation")
elif(T>40 and T<=55):
     print("Teampreature is very hot out side and medium  uv radiation ")
elif(T>55 and T<=70):
     print("Teampreature is very hot out side and very high  uv radiation .\n stay at home and drick water too much time to time")
else:
    print("Enter valid teampreature")
