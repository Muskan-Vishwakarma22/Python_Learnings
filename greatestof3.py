#Greatest of three numbers

a = input("Enter the first number: ")
if "." in a:
    a = float(a)
else:
    a = int(a)
b = input("Enter the second number: ")
if "." in b:
    b = float(b)
else:
    b = int(b)
c = input("Enter the third number: ")
if "." in c:
    c = float(c)
else:
    c = int(c)
if (a>b and a>c):
    print(a,"a is the greatest number")
elif b>a and b>c:
    print(b,"b is the greatest number")
elif c>a and c>b:
    print(c,"c is the greatest number")
elif (a==b==c==a):
    print("Invalid Input")
else:
    print("Invalid input")
#When a=b=c: the o/p is in the else statement
#o/p: Invalid input
#When 2 i/p are common and they are greater than the third variable then it will generate the else o/p i.e Invalid input
