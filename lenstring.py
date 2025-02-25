#To find the length of string without using len function
a = input("Enter the string: ")
length = 0 #Update variable
for i in a:
    length += 1
print("The length of string",a,"is:",length)