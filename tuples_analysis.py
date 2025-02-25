mytuple = () #Initialize a tuple
print(type(mytuple))
mytuple1 = (1,2,3,4)
mytuple2 = (10.2,10.4,10.16,20.8)
mytuple3 = ("Viren","Shlok","Nair","Tyagi")
# mytuple4 = ("Shivansh","Yuvika",1,99.6)
# mytuple5 = (1,1,2,3,3,567,67,67,567,2)

#PRINTING TUPLE
print(mytuple3)
print(mytuple3[0])
# print(mytuple3(0)) #TypeError: 'tuple' object is not callable
# mytuple3[2]= 30 #TypeError: 'tuple' object does not support item assignment
# t3 = ()
# print(t3 = mytuple1+mytuple2) #t3 = mytuple1+mytuple2
t1 = (1,2,3)
# print(t1)*3 #TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print(t1*3)
print((t1)*3)  #SAME O/P
"""(1, 2, 3, 1, 2, 3, 1, 2, 3)
(1, 2, 3, 1, 2, 3, 1, 2, 3)"""
