################################################### decision_making ############################################
# used for make decision based on condition
# 4 types
# 1. if
# 2. if--else
# 3. if--elif--else
# 4. nested

# 1. if
# syntax
# if(cond):
# statement

n = int(input("Enter a Postive Number :-"))
if(n>0):
    print(n)
print("Congrats try this one")


# 2. if--else
# syntax
# if(cond1):
# statement
# else(cond2):
# statement

# check whether number is postive or negative
n = int(input("Enter a Number :-"))
if(n>0):
    print("Input",n,"is a positive Number")
else:
    print("Input",n,"is a negative Number")    
print("Congrats try one more")

# check whether number is odd or even
m = int(input("Enter a Number :-"))
if(m%2==0):
    print("Input",m,"is a even Number")
else:
    print("Input",n,"is a odd Number")
print("Congrats try one more")

# check whether number is three digit
o = int(input("Enter a Number :-"))
if(100<=o<=999):
    print("Input",o,"is a three digit Number")
else:
    print("Input",o,"is not a three digit Number")
print("Congrats try one more")

# check whether number is divisible by 5 and 7
p = int(input("Enter a Number :-"))
if(p%5==0 and p%7==0):
    print("Input",p,"is divisible by 5 and 7")
else:
    print("Input",p,"is not divisible by 5 and 7")
print("Congrats try one more")

# check which number is greater
q = int(input("Enter a First Number :-"))
r = int(input("Enter a Second Number :-"))
if(q>r):
    print("Input",q,",first number is biggest")
else:
    print("Input",r,",second number is biggest")
print("Congrats try one more")

# check whether alphabet is vowel or not
s = input("Enter a character :-")
if(s=="a" or s=="e" or s=="i" or s=="o" or s=="u" or s=="A" or s=="E" or s=="I" or s=="O"  or s=="U"):
    print(s,"is a vowel")
else:
    print(s,"is not a vowel")

# or
t = input("Enter a character :-")
vowels=['a','e','i','o','u','A','E','I','O','U']
if (t in vowels):
    print(t,"is a vowel")
else:
    print(t,"is not a vowel")


# 3. if--elif--else
# syntax
# if(cond1):
# statement
# elif(condn):
# statement
# else:
# statement

# check which number is greater
u = int(input("Enter ++a First Number :-"))
v = int(input("Enter a Second Number :-"))
w = int(input("Enter a Third Number :-"))
if(u>v and u>w):
    print("Input",u,",first number is biggest")
elif(v>u and v>w):
    print("Input",v,",first number is biggest")
else:
    print("Input",w,",second number is biggest")
print("Congrats all over")

