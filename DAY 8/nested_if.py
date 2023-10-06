############################################### nested if #########################################################
# if condition inside another if condition
# Syntax

# if (cond):
#     if(cond):
#         statement
#     else:
#         statement
# else:
#     if(cond):
#         statement
#     else:
#         statement

# divisibility check on 2 and 3
print("Welcome check the divisibility")
a = int(input("Enter the a number :- "))
if (a%2==0):
    if(a%3==0):
        print(a,"is divisible by 2 and 3")
    else:
        print(a,"is only divisible by 2")
else:
    if(a%3==0):
        print(a,"is only divisible by 3")
    else:
        print(a,"is not a divisible both 2 and 3")
print("Thank You")