# 1,3,5,7,9,11
sum = 0
product = 1
for i in range (1,12,2):
    sum = sum+i
    product = product*i
print(sum)
print(product)

# 5,10,15,20,25,30

sum = 0
product = 1
for i in range (5,31,5):
    sum = sum+i
    product = product*i
print(sum)
print(product)

# 2,4,6,8,10

sum = 0
product = 1
for i in range (2,11,2):
    sum = sum + i
    product = product * i
print(sum)
print(product)

# 1,8,15,22,29,36

sum = 0
product = 1
for i in range (1,37,7):
    sum = sum + i
    product = product * i
print(sum)
print(product)

# 5,4,3,2,1

sum = 0
product = 1
for i in range (5,0,-1):
    sum = sum - i
    product = product * i
print(sum)
print(product)

# Count of 3 digit numbers that are divisible 3 in range (100,1000)

# count = 0
# for i in range(100,1000):

# Using index value

s = "rajesh"
for i in range (0,6,2):
    print(s[i])

# count and sum of positive even numbers

s = [67,14,23,8,-5,-12,-6]
sum = 0
count = 0
for i in s:
    if(i>0 and i%2==0):
        sum = sum + i
        count = count + i
print(sum)
print(product)

# count of int,floats,str

s = ['hello',9.8,'a',7.5,9,5,1.5,6]

c1 = 0
c2 = 0
c3 = 0
for i in s:
    if (type(i)==str):
        c1 = c1+1
    elif (type(i)==int):
        c2 = c2+1
    elif (type(i)==float):
        c3 = c3+1
    else:
        print("invalid")
print("Number of string : ",c1)
print("Number of integer : ",c2)
print("Number of float : ",c3)
