x=float(input("Enter x axis of point:"))
y=float(input("Enter y axis of point:"))
if( x==0 and y==0):
    print("Point lies on origin.")
elif( x==0 and y>0):
    print("Point lies on positive Y axis.")
elif( x==0 and y<0):
    print("Point lies on negative Y axis.")
elif( x>0 and y==0):
    print("point lies on positive X axis")
elif( x<0 and y==0):
    print("point lies on negative X axis")
elif(x>0 and y>0):
    print("point lies in FIRST QUADRANT")
elif(x>0 and y<0):
    print("point lies in FOURTH QUADRANT")
elif(x<0 and y<0):
    print("point lies in THIRD QUADRANT")
else:
    print("point lies in SECOND QUADRANT")
