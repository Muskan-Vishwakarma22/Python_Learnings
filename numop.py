#PLAYING WITH DIFFERENT TYPES OF OPERATIONS ON DIFFERENT CASES OF INTEGERS AND OBSERVING DIFFERENT TYPES OF ERRORS
#CASE1 both +ve
# a = 50
# b = 33 
# print(a -b)
# c = a - b
# print(c)
# print(a * b)
# print(a / b)
# d = a * b
# print(d)
# d = a//b
# print(d)

#CASE 2 both -ve
# a = -22
# b = -10
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# output
# -30
# -10
# 200
# 2.0
# 2

#CASE 3: a +ve and b -ve
# a = 29
# b = -20
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# output
# 9
# 49
# -580
# -1.45
# -2

# CASE 3.1
# a = 10
# b = -0
# print(a + b)
# print(a - b)
# print(a * b)

# output
# 10
# 10
# 0
# print(a / b)
# #ZeroDivisionError: division by zero

# print(a // b)
# #ZeroDivisionError: integer division or modulo by zero
# print(a % b)

# #ZeroDivisionError: integer modulo by zero
# print(a ** b) #o/p: 1

# CASE 3.2
# a = 0 
# b = -10
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
'''
OUTPUT:
-10
10
0
-0.0
0
0
ZeroDivisionError: 0.0 cannot be raised to a negative power
Observation: 0 can't be raised to -ve power
'''
# CASE 3.3
# a = 5
# b = -2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

'''
OUTPUT
3
7
-10
-2.5
-3
-1
0.04
'''

#CASE 4: a -ve and b +ve
# a = -29
# b = 20
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# output
# -9
# -49
# -580
# -1.45
# -2

#FLOAT CASES 
# a = 5.3
# b = 3.3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# output 
# 8.7
# 1.9
# 18.02
# 1.5588235294117647
# 1.0
# 1.2999999999999998
# a = 10

# print(a, "is the value")


