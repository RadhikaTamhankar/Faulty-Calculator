print("Enter first no.")
x=int(input())
print("enter your operation")
y=input()
print("enter second no.")
z=int(input())
if x==45 and y=="*" and z==3:
    print("555")
elif  x==56 and y=="+" and z==9:
    print("77")      
elif x==56 and y=="/" and z==6:
    print("4")
elif y=="+":
    c=x+z 
    print(c)
elif y=="-":
    d=x-z 
    print(d)
elif y=="*":
    c=x*z
    print(c)
else:
    f=x/z
    print(f)  
