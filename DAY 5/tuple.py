############################################ Tuple #############################################################
# 1. Collection of IMMUTABLE
# 2. Allow Dupltication
# 3. Ordered collection
# collection of different types of datatypes elements
# Representation ( )

# Syntax

Tuple = (1,2,3,4)
print("Tuple :-" ,Tuple)

Fruit = ('apple','banana','mango')

# Length of tuple
print(len(Fruit))
# id of tuple
print(id(Fruit))
# index
a = Fruit.index("apple")
print("Index value of apple :- ",a)
b = Fruit.count("banana")
print("No.of banana in fruit using count :- ",b)

# Note : * Tuple are sequence just like list. The difference between tuple and list are 
#          tuples cannot be changed unlike list can 
#         * tuples use paratheses but list use square bracket []
