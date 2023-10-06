print("Enter the three sides of triangle")
s1 = int(input("Enter the First side :- "))
s2 = int(input("Enter the Second side :- "))
s3 = int(input("Enter the Third side :- "))
if(s1 == s2 and s2 == s3):
    print("It is an Equailateral Triangle")
elif(s1 == s2 or s2 == s3 or s1 ==s3):
    print("It is an Isosceles Triangle")
else:
    print("It is an Scalene Triangle")
