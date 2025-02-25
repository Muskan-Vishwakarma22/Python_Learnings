#TESTING WITH LISTS AND LIST METHODS 
list1 = [] #DECLARING EMPTY LIST
mylist = ["one","two"]
#LIST consisting of string and list
#SETS, LISTS AND STRING IN A SET 
list2= ["Asif",25,[50,100],[15,20]]

#TRIAL
list1= [1,2,3]
print(len(list1))
list2= [1,[2,3]]
print(len(list2))
print(len(list2[1]))
list3 = [1,[2,3],{4,5}]
print("INDEX INSIDE LIST")
print(list3[1][0])
print(len(list3))
print(len(list3[1]))
print(len(list3[2]))
list4 = [1,{2,3}]
print(len(list4))

#ADD ELEMENTS IN A LIST
mylist.append("nine")
print(mylist)
#Extend function
# mylist.extend("Hi","Muskan") #TypeError: list.extend() takes exactly one argument (2 given)
mylist.insert(9,'ten')
print(mylist)
# mylist.insert(9) #TypeError: insert expected 2 arguments, got 1
# print(mylist)
print(my)
print(mylist.pop())#takes index as an argument
print(mylist)
#JOIN LISTS
list1 = list1+list2
#MEMBERSHIP
#Reverse list

mylist.reverse()
