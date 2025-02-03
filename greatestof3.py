#Greatest of three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b and a>c:
    print(a,"a is the greatest number")
elif b>a and b>c:
    print(b,"b is the greatest number")
elif c>a and c>b:
    print(c,"c is the greatest number")
else:
    print("Invalid input")