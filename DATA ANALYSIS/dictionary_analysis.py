# d = {"Fruit": "Apple,Mango","Colour": "Red,Yellow"}
# print(d)
a = {} #Initialize an empty dictionary
print(type(a)) #<class 'dict'>
for i in a:
    print(i) #Print nothing
#INITIALIZE A DICTIONARY
a = {"colour":"green","fruit":"apple","placeofprod":"Shimla"}
new = dict(m = "muskan",t = "tyagi",s="Shreya",sam="samarth")
print(new)
for i in a:
    print(i) #returns the keys of dictionary
print(a.keys) #<built-in method keys of dict object at 0x000002AF714AB880>
print(a.keys())
print(a) #displays the dictionary
for i in enumerate(a):
    print(i)
print(a.values())
a["fruit"]="guava"
print(a["fruit"])
print(a.get("fruit")) #Value linked with key fruit is guava
print(a.get("fruits")) #re
# a.pop()#TypeError: pop expected at least 1 argument, got 0
# a.pop[1] #TypeError: 'builtin_function_or_method' object is not subscriptable
# a.pop(1) #KeyError: 1
# a.pop([1]) #TypeError: unhashable type: 'list'
a.pop("fruit") #deleted the value linked with key "fruit"
print(a) #{'colour': 'green', 'placeofprod': 'Shimla'}
c = {"colour":{"green","red"},"fruit":"apple","placeofprod":"Shimla"}
#how to find length of a dictionary
print(len(c))

#RETURN ITEMS
print(c.items())
print(c.popitem()) # removes and returns the last inserted key-value pair as a tuple

