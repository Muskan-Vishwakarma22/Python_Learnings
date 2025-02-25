#CODE FOR FIBONACCI SERIES
n = int(input("Enter the number of elements: "))
a = 0
b = 1
print("The fibonacci series is: ")
print(a)
print(b)
for i in range(2,n):
    c = a+b
    print(c)
    b,a = c,b