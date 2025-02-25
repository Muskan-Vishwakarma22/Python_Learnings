#Program to check if the given number is armstrong number
arm = int(input("Enter the Number to check armstrong: "))
arm =str(arm)
up = 0
digits = sum(1 for i in arm if i.isdigit())
for i in arm:
    up += pow(int(i),digits)
print(up)
if str(up) == arm:
    print("Armstrong")
else:
    print("Not Armstrong")    
