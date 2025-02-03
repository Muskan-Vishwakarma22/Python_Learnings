#PYTHON STRINGS
#SLICING
#String Literals
# print(""" my name is
      # jih""")
# a = """Hello
# my name is
# muskan"""
# 


a = "hivirenderpython"
#SLICING
#BOTH POSITIVE
print(a[1:4])
#OUTPUT: ivi

print(a[4:1])
#OUTPUT:
# (Empty line)

print(a[1:1])
#OUTPUT:
# (Empty line)


#BOTH NEGATIVE
print(a[-1:-4])
#OUTPUT 
# (Empty line)

#OBSERVATION: Backwards slicing is not possible(from right to left)
#Starting index must be smaller than stopping index(ONLY FOR POSITIVE)
print(a[-4:-1])
#OUTPUT 
#tho 
#(starting from -4 index and stopping at a poition before -1) hence the end value is not included 

print(a[-1:-1])
#OUTPUT:
# (Empty line)

#EITHER +ve or -ve
#st =-ve sp +ve
print(a[-1:4])
#OUTPUT 
# (Empty line)

print(a[-4:1])
#OUTPUT 
#Empty o/p : right to left not working

print(a[-4:14])
#OUTPUT
#th (left to right)

#st+ve  sp -ve
print(a[1:-4])
#OUTPUT
# ivirenderpy

print(a[4:-1])
#OUTPUT
#renderpytho

print(a[10:-10])
#NO OUTPUT(Empty)
print(a[20:4])
#NO OUTPUT(Empty)

print(a[1:15:2])
#OUTPUT
#iiedryh

print(a[0:10:0]) #ValueError: slice step cannot be zero
print