#PERFORMING DIFFERENT TYPES OF FUNCTIONS ON STRINGS
a = " Hi Muskan Vishwakarma  "
print(a)
print(a.strip()) #hi muskan vishwakarma(removes spaces from left and right)
# print(strip(a)) #NameError: name 'strip' is not defined
print(a.lower())
# print(a.strip.lower()) #AttributeError: 'builtin_function_or_method' object has no attribute 'lower'
print(a.strip().lower())#hi muskan vishwakarma
print(a.lower().strip())#hi muskan vishwakarma
print(a.upper())
print(a.replace("a","A")) # Hi MuskAn VishwAkArmA
print(a.replace("a","_")) # Hi Musk_n Vishw_k_rm_
print(a.count(a))

#MEMEBERSHIP OPERAT03
y1 = "muskan" in a
print(y1) #False
y2 = "Muskan" in a
print(y2) #True

y3 = "Muskan" not in a
print(y3)

print(y1+y2) #BOOLEAN ADDITION: O/P: 1

b = "Hello"
print(b+a) #STRING CONCATENATION: Hello Hi Muskan Vishwakarma

a1 = True
a2 = True
a3 = False
print(a1+a2) #o/p : 2
print(a3+a3) #o/p : 0

# a = Tru #NameError
# print(a+a1)

a = "Tru"
# print(a+a1) #TypeError: can only concatenate str (not "bool") to str
print("The value of m is 10") #print the same string
a =10
b =20
c = "The value of a is : {}\n" #place holders 
c = "The value of a is : {}"
print(c.format(a))#The value of a is : 10
print("the value of c is: ",c)
d = 20
print("The value of c is:",d)
c = "The value of a is : {},{},{}"
# print(c.format()) #IndexError: Replacement index 0 out of range for positional args tuple
print(c.format(a,a,a)) #The value of a is : 10,10,10
c = 
new = "The value of a is"
print(new.format(a,a)) #The value of a is

