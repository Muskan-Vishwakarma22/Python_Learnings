#Aim: Program to find the lcm of two numbers number
# numbers = input("Enter the numbers you want to find LCM of: ")

# terms = numbers.split(" ")

# for i in range(len(terms)):
#     terms[i] = int(terms[i])
# factors =[]

# if len(terms) == 1:
#     print(terms[0])
#     exit()
# elif len(terms) > 1:
#     for i in terms:
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 factors.append(j)
#             else:
#                 continue

# print(factors)
# lcm = 1
# for i in factors:
#     if factors.count(i) != 1:
#         lcm = lcm * i

# print(lcm)

# Taking input for number of elements
n = int(input("Enter the number of numbers: "))

numbers = input("Enter the numbers separated by spaces: ").split()

if n == 1:
    print(numbers[0])
else:
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    
    # Finding LCM of first two numbers
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    
    # Finding LCM iteratively for remaining numbers
    for i in range(2, n):
        num = int(numbers[i])
        greater = lcm if lcm > num else num
        while True:
            if greater % lcm == 0 and greater % num == 0:
                lcm = greater
                break
            greater += 1

    print("LCM:", lcm)