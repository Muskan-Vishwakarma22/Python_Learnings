a = {}
print(type(a)) #<class 'dict'>
a = []
print(type(a)) #<class 'list'>
a = {1,2}
print(type(a)) #<class 'set'>
a = set()
print(type(a)) #<class 'set'>
a = {1,2,3,1,2}
print(len(a)) #3
print(a) #{1, 2, 3}
a = {"apple","mango","cherries"}
print(a)
a = {1,"apple",2,"mango"}
print(a)

# a = {1,[2,3,4]}
# print(a) #TypeError: unhashable type: 'list'
# a = set(1,2,3,4) #TypeError: set expected at most 1 argument, got 4
a = set((1,2,3,4))
print(a)

# a = {a1,a2,a3,a4} #NameError: name 'a1' is not defined. Did you mean: 'a'?
# for i in a:
    # print(i)
a = {"a1","a2","a3","a4"}
for i in a :
    print(i)
# for i in len(a):
#     print(i) #TypeError: 'int' object is not iterable
for i in range(0,len(a)):
    print(i)
'''0
1
2
3'''
for i in enumerate(a):
    print(i)
'''
(0, 'a1')
(1, 'a4')
(2, 'a3')
(3, 'a2')'''
print("--------------------")
#18 feb 2025
myset = {10,2,33,400,5,6,7,8}
for i in enumerate(myset):
    print(i)
myset = {"eight","five","four","one","seven","six","three","two"}
myset.add('NINE')
print(myset)
myset.add(9)
print(myset)
# myset.add(nine) #NameError: name 'nine' is not defined. Did you mean: 'None'?
print("-----------------")
# myset.add(input())
print(myset)
# myset.add(input(),input()) #TypeError: set.add() takes exactly one argument (2 given)

#UPDATE SET
# myset.update(9) #TypeError: 'int' object is not iterable
print(myset)
# myset.update(nine) #NameError: name 'nine' is not defined. Did you mean: 'None'?
# print(myset)
myset.update("Nine")
print(myset)
print("-----------------")
#SET OPERATIONS
A = {1,2,3,4,5}
B ={4,5,6,7,8}
C = {8,9,10}
#UNION
print(A|B)
print(A.union(B)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B,C)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#INTERSECTION
print("----------------")
print(A&B)
print(A.intersection(B))
# A.intersection_update(B) #A=A-B
# print(A)
'''{4, 5}
{4, 5}
{4, 5}'''
new = {2,3,4,{2,3}}
print(new)