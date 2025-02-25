#factorial of a number
n = input("Enter the number: ")
fact = 1
while (type(n)!=int):
   if (n==0)or(n==1):
      fact = 1
   elif n<0:
      print("Invalid Input")
   for i in range(1,n+1):
      fact *= i
   print(fact)
print("Inavlid Input")

#factorial of a number
# n = int(input("Enter the number: "))
# fact = 1
# if (n==0)or (n==1):
#   fact = 1
# elif n<0:
#    print("Invalid Input")
# else:
#    for i in range(1,n+1):
#     fact *= i
#    print(fact)
   


   