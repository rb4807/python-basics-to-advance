########################################### Dictionary ##########################################

# Collection of KEY, VALUE pair
# Mutable
# Representation { 'key' : 'value' }

# Syntax

Dictionary ={name:'Arun', age:24, course :'MEAN'}
print("Dictionary :-" ,Dictionary)

# assigning value in list format

d={101:['Arun',23,'Python'],102:['Aju',24,'MERN'],103:['Balu',25,'MEAN'],}
print(d)
print(d[101])
print(d[102][0])

# assigning value of dictionary to a1

f1 = d[101][1]
print(f1)

# finding average of above data

e1 = d[101][1]
e2 = d[102][1]
e3 = d[103][1]
total = e1+e2+e3
avg = total/3
print("average : ",avg)

# assigning value in dictionary format

b = {   101 : {'name' : 'Arun', 'age':23, 'course' :'Python'},
        102 : {'name' : 'Achu', 'age':24, 'course' :'MERN'},
        103 : {'name' : 'Balu', 'age':25, 'course' :'MEAN'}
    }
print(b)
print(b[101])
print(b[102]['name'])

# assigning value of dictionary to a1

g1 = b[101]['age']
print(g1)

# finding average of above data

a1 = b[101]['age']
a2 = b[102]['age']
a3 = b[103]['age']
sum = a1+a2+a3
average = sum/3
print("average : ",average)