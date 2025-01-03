a=float(input("enter 1st num:"))
b=float(input("enter 2nd num:"))
print("press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division\npress 5 for square\npress 6 for cube")
choice=int(input("enter your choice between 1-4:"))
if choice==1:
	print(a,"+",b,"=",a+b)
elif choice==2:
	print(a,"-",b,"=",a-b)
elif choice==3:
	print(a,"*",b,"=",a*b)
elif choice==4:
	print(a,"÷",b,"=",a/b)
elif choice==5:
	print(a,"²=",a**2)
	print(b,"²=",b**2)
elif choice==6:
	print(a,"³=",a**3)
	print(b,"³=",b**3)
else:
	print("invalid input")