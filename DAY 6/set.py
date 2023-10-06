########################################## Sets #############################################################

# collection of different types of elements
# 1. Only Unique elements(no duplication)
# 2. Only Immutable elements(num,string,tuple)
# 3. Unordered collection (unpredictable because if we type index value of element it will returns error)
# Representation { }

# Syntax

Set = {1,2,3,4}
print("Set :-" ,Set)

Fruit = {'apple','banana','mango','Papaya'}
print("Fruit :- ",Fruit)
#  add
Fruit.add("orange")
print("Fruit after append :- ",Fruit)
# copy
a = Fruit.copy()
print("Copied all elements from fruit to a :- ",a)

Fruits = {'pineapple','grape','mango'}
print("Fruits :- ",Fruits)

# intersection
b = Fruit.intersection(Fruits)
print("intersection between Fruit and Fruits :- ",b)
# isdisjoint
c = Fruit.isdisjoint(Fruits)
print("If common elements it will be false else true using is disjoint:- ",c)
# issubset
d = Fruit.issubset(Fruits)
print("If all Fruit elements are present in Fruits it will be true else false using is issubset:- ",d)
# issuperset
d = Fruit.issuperset(Fruits)
print("If all Fruits elements are present in Fruit it will be true else false using is issubset:- ",d)
# difference
e = Fruit.difference(Fruits)
print("Difference between Fruit and Fruits :- ",e)
# symmetric_difference
f = Fruit.symmetric_difference(Fruits)
print("symmetric_difference between Fruit and Fruits :- ",f)
# union
g = Fruit.union(Fruits)
print("union between Fruit and Fruits :- ",g)
# update
Fruit.update(Fruits)
print("update between Fruit and Fruits :- ",Fruit)
# discard
Fruit.discard("banana")
print("Banana removed from fruit by specifing position :- ",Fruit)
# remove
Fruit.remove('apple')
print("apple removed from fruit by specifing position :- ",Fruit)
# pop
Fruit.pop()
print("Remove last element :- ",Fruit)
# pop
Fruit.clear()
print("Remove all element :- ",Fruit)