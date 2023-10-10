# Write a program to find the count of numbers in the range (100,1000) that are divisible by 3

i = 100
count = 0
while(i<=1000):
    if(i%3==0):
        count = count + 1
    i = i+1
print(count)

# sum,product

sum = 0
product = 1
i = 1
while(i<=5):
    sum=sum+i
    product=product*i
    i=i+1

print(sum)
print(product)

# 1,3,5,7,9,11(sum,product)

sum = 0
product = 1
i = 1
while(i<=11):
    sum=sum+i
    product=product*i
    print(i)
    i=i+2
print(sum)
print(product)

# 2,4,6,8,10(sum,product)

sum = 0
product = 1
i = 2
while(i<=10):
    sum=sum+i
    product=product*i
    print(i)
    i=i+2
print(sum)
print(product)

# 5,10,15,20,25,30(sum,product)

sum = 0
product = 1
i = 5
while(i<=30):
    sum=sum+i
    product=product*i
    print(i)
    i=i+5
print(sum)
print(product)

# 4,9,14,19,23,29,34(sum,product)

sum = 0
product = 1
i = 4
while(i<=34):
    sum=sum+i
    product=product*i
    print(i)
    i=i+5
print(sum)
print(product)

# 4,9,14,19,23,29,34(sum,product)

sum = 0
product = 1
i = 4
while(i<=34):
    sum=sum+1**3
    product=product*i
    print(i)
    i=i+5
print(sum)
print(product)

# Factorial of a number
n=int(input("Enter a number :- "))
fact = 1
i = 1
while(i<=n):
    fact=fact*i
    i=i+1
print("Factorial of",n,"is",fact)