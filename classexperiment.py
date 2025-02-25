#EXPERIMENT 
#DATE: 25 February 2025
# QUESTION 1
#WAP to scan n values in range 0 to 3 and print the number of times each value has occured 

#CASE 1: only the valid inputs will be counted in n
# n = int(input("Enter the number of values you want to input: "))
# list1 = []
# while(len(list1)<n):
#     num = int(input("Enter the number in range 0 to 3: "))
#     if (num < 0 or num > 3):
#         print("Invalid Input")
#     else:
#         list1.append(num)
# for j in range(0,4):
#     print("The occurence of",j,"is: ",list1.count(j))

#CASE 2: both the valid and invalid inputs will be counted in n
# list1 = []
# n = int(input("Enter the number of values you want to input: ")) 
# for i in range(n):
#     num = int(input("Enter the number in range 0 to 3 "))
#     if (num>3 or num<0):
#         print("Invalid Input")
#     else:
#         list1.append(num) 
# for j in range(0,4):
#     print("The count of",j,"is",list1.count(j))

#QUESTION 2
#WAP to CREATE a tuple to store n numberic values and find average of all values
# a1 = []
# a = ()
# n = int(input())
# for i in range(n):
#     a1.append(int(input()))
# a = tuple(a1)
# avg = 0
# for i in a:
#     avg = avg+i
# print(avg/n)

#WAP to input a list from user and display the maximum and minimum element from the list
# a = []
# n = int(input("Enter the number of elements"))
# for i in range(n):
#     a.append(int(input("Enter the element: ")))
# print("the list is: ",a)
# print("Maximum element: ",max(a))
# print("Minimu Element: ",min(a))

#SYNTAX TO TAKE MULTIPLE INPUTS IN A SINGLE LINE SEPERATED BY SPACES OR ANY CHARACTER
# b = map(int,input("Enter the elements seperated by spaces: ").split())
# print(list(b))

#WAP to reverse a list
# b = []
# a =[10,20,30,40,50]

#REVERSE LIST USING OTHER LIST
# for i in range(len(a),0,-1):
#     b.append(a[i-1])
# print(b)

# #REVERSE LIST WITHOUT USING OTHER LIST WITH THE HELP OF INDEXING AND SWAPPING 
# temp = 0
# for i in range(0,len(b)//2):
#     temp = b[i]
#     b[i] = b[len(b)-i-1]
#     b[len(b)-i-1] = temp
# print(b)
# print(a)

#PROGM TO REMOVE DUPLICATE ITEMS FROM A LIST
#1. USING FOR AND WHILE LOOPS
new  = [10,10,20,5,10,9,5]
# for i in new:
#     while i in new:
#         new.remove(i)
# print(new)

# unique_list = []

#USING OTHER LIST
# for x in new:
#     if x not in unique_list:
#         unique_list.append(x) 

# print(unique_list) #DISPLAYS DISTINCT ELEMENTS

#USING SETS
# print(list(set(new))) #DISPLAYS DISTINCT ELEMENTS BUT IN AN UNORGANIZED MANNER