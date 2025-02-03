#if_else statements
#Make a calculater using user input of two numbers (addition,subr=traction,multiplication and division)
a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))
print("OPTIONS \n1.Addition(+)\n 2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\nEnter the choice")
choice = int(input())
if choice == 1:
    print("The sum of",a,"and",b,"is",a+b)
elif choice == 2:
    print("The difference of",a,"and",b,"is",a-b)
elif choice == 3:
    print("The product of",a,"and",b,"is",a*b)
elif choice == 4:
    print("The division performed on",a,"and",b,"is",a/b)
else:
    print("Invalid input")
    exit(0)

