#to calculate the sum of all the numbers from 1 to n
sum = 0
n = int(input("Enter the number: "))
for i in range(1,n+1):
    sum += i
print("The sum of all the numbers from 1 to n is: ",sum)