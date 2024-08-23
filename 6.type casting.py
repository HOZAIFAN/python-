# this is implicit type casting
a=5 #integer it will automatically converted into float by compiler
b=2.5 #float 
print("THE SUM IS ",a+b) 
#this is explicit type casting
a="5" #int  this will not convert into float
b=7.5
c=int(a)
print("THIS IS EXPLIXIT TYPE CASTING",b+c)
#this is  annother explixit type casting
a=2.5
b=5.8
c=a+b
d=int(c) #the result of float is converted into int
print("THIS IS ANOTHERR EXPLIXIT TYPE CASTING",d)
