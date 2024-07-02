a=int(input("enter the number : "))
b=int(input("enterthe second number : "))
c=int(input("enter the third number : "))
 
if(a>=b and a>=c):
    print("The a is greater than b and c")
elif(b>=a and b>=c ):
    print("The b is greater than a and c")
elif(c>=a and c>=b):
    print("The c is greater than b and c")