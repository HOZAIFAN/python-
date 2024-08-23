pin=int(input("WELCOME! Enter your pin:"))
import time 
if(pin==8003):
    time.sleep(3)
    amount=int(input("ENTER YOUR AMOUNT:"))    
#this will delay output for thee second giving real filling of atm machine
    time.sleep(3)
    print("Take your",amount,"cash and your slip" )
    time.sleep(3)
    print("THANK YOU FOR YOUR TRANSACTION:")
else:
    time.sleep(3)
    print("YOUR CODE IS INCORRECT PLZ TRIANGAIN.")