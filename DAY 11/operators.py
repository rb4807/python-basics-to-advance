#################################################### Operators ###########################################################

# 1. Arithmetic Operators :- +, -, *, /, %, //, **

a = 1+2
print(a)

a = 2-1
print(a)

a = 2*2
print(a)

a = 10/2
print(a)

a = 10%2
print(a)

a = 10//2
print(a)

a =10**2
print(a)

# 2. Assignment Operators :- =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=

a = 1
b = a
print(b)

a = 1 
a += 3
print(a)

a = 5
a -= 1
print(a)

a = 5
a *= 2
print(a)

a = 10
a /= 2
print(a)

a = 10
a %= 2
print(a)

a = 10
a //= 2
print(a)

a = 10
a **= 2
print(a)

a = 10
a &= 2
print(a)

a = 10
a |= 2
print(a)

a = 10
a ^= 2
print(a)

a = 10
a >>= 2
print(a)

a = 10
a <<= 2
print(a)

# 3. Logical Operators :- AND, OR, NOT

n = 10
print( n%5==0 and n%3==0 )

n = 10
print(n>0 or n<7 )

n = 10
print(not( n%5==0 and n%3==0 ))

# 4. Comparison Operators (Relational Operators) :- ==, !=, >, <, <=, >=

a = 2
b = 3
print (a==b)

a = 2
b = 3
print (a!=b)

a = 2
b = 3
print (a>b)

a = 2
b = 3
print (a<b)

a = 2
b = 3
print (a<=b)

a = 2
b = 3
print (a>=b)

# 5. Bitwise Operators :- &(AND), |(OR), ^(XOR), ~(NOT), <<(LEFT SHIFT), >>(RIGHT SHIFT)

print(6 & 2)

print(6 | 2)

print(6 ^ 2)

print(~ 2)

print(6 >> 2)

print(6 << 2)

# 6. Membership Operators :- in, not in

x = ["apple","mango","grape"]
y = ["apple","mango"]
print(x in y)

x = ["apple","mango","grape"]
y = ["apple","mango"]
print(x not in y)

# 7. Identity Operators :- is , is not

# To check ID of two values is same

x = ["apple","mango","grape"]
y = ["apple","mango"]
print(x is y)

x = ["apple","mango","grape"]
y = ["apple","mango"]
print(x is not y)
