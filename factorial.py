#factorial of a number
n = int(input("Enter the number you want to find the factorial of"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)