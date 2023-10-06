print("Hello")
a = int(input("Enter the First Number :- "))
b = int(input("Enter the Second Number :- "))
print("Operations :- \n 1. Addition(+) \n 2. Subtraction(-) \n 3. Multiplication(*) \n 4. Division(/)")
op = int(input("Please select the operation :- "))
if(op==1):
    c = a+b
    print("Result = ",c)
elif(op==2):
    c = a-b
    print("Result = ",c)
elif(op==3):
    c = a*b
    print("Result = ",c)
else:
    c = a/b
    print("Result = ",c)