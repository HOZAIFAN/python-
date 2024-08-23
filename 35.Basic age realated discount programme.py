age=float(input("Enter your age:"))
if(age>0):
#here disc represent discount
    if(age>0 and age<=10):
        print("You will got 50% discount on your item.")
        price=float(input("Enter prize of your item:"))
        disc=price*(50/100)
        discprice=price-disc
        print("you got",disc,"RS discount.\nDiscounted price of your item is:",discprice)
    elif(age>10 and age<=20):
        print("You will got 30% discount on your item")
        price=float(input("Enter prize of your item:"))
        disc=price*(30/100)
        discprice=price-disc
        print("you got",disc,"RS discount.\nDiscounted price of your item is:",discprice)
    elif(age>20 and age<=30):
        print("You will got 20% discount on your item.")
        price=float(input("Enter prize of your item:"))
        disc=price*(20/100)
        discprice=price-disc
        print("you got",disc,"RS discount.\nDiscounted price of your item is:",discprice)
    elif(age>30 and age<=50):
        print("You will got 10% discount on your item.")
        price=float(input("Enter prize of your item:"))
        disc=price*(10/100)
        discprice=price-disc
        print("you got",disc,"RS discount.\nDiscounted price of your item is:",discprice)
    else:
        print("Sorry you will have no discount.")

else:
    print("invalid age")
    
    