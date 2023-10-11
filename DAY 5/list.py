############################################ List #############################################################
# collection of different types of datatypes elements
# 1. Collection of MUTABLE
# 2. Allow Dupltication
# 3. Ordered collection
# Representation [ ]

# Syntax

List = [1,2,3,4]
print("List :-" ,List)


Fruit = ['apple','banana','mango']
print("Fruit :- ",Fruit)

# Length of list
print(len(Fruit))
# id of list
print(id(Fruit))
#  append
Fruit.append("orange")
print("Fruit after append :- ",Fruit)
# pop
Fruit.pop(3)
print("Fruit after pop :- ",Fruit)
# reverse
Fruit.reverse()
print("Fruit after reverse :- ",Fruit)
# index
a = Fruit.index("apple")
print("Index value of apple :- ",a)
# extend
new = ['banana','watermelon','pineapple']
Fruit.extend(new)
print("Fruit after extend :- ",Fruit)
# count
b = Fruit.count("banana")
print("No.of banana in fruit using count :- ",b)
# insert
Fruit.insert(1,"lemon")
print("Fruit after insert by specified position :- ",Fruit)
# copy
c = Fruit.copy()
print("Copied all elements from fruit to c :- ",c)
# sort
Fruit.sort()
print("Fruit sorted :- ",Fruit)
# remove
Fruit.remove('banana')
print("Banana removed from fruit by specifing position :- ",Fruit)
# clear
Fruit.clear()
print("removed all elements from fruit by clear :- ",Fruit)