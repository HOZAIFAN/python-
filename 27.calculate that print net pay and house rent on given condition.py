# 'bp' is basic pay   'np' is netpay  'hr' is house rent
bp=float(input("Enter basic pay:"))
if(bp<30000 and bp>0):
    hr=bp*(30/100)
    np=bp+hr
    print("The net pay is:",np,"\n House rent is:",hr)
elif(bp>=30000 and bp<=50000):
    hr=bp*(35/100)
    np=bp+hr
    print("The net pay is:",np,"\n House rent is:",hr)
elif(bp>50000):
    hr=bp*(40/100)
    np=bp+hr
    print("The net pay is:",np,"\n House rent is:",hr)
else:
    print("Enter valid basic pay again")

  