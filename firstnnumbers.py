#WAP to print first n natural numbers from 1 to the number input by user
num = input("Enter the number: ")
if type(num)==complex:
    print("Inavlid Input")
elif type(num)==float:
    print("Inavlid Input")
else:
    # num = int(num)
    i = 1
    while(i<=num):
        print(i)
        i+=1
