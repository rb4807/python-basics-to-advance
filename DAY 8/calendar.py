print("Choose your to month to check number of day have. \n January February March April May June July August September October November December ")
a = ['January','March','May','July','August','October','December']
b = ['April','June','September','November']
month = (input("Enter the month :- "))

if(month in a):
    print(month," have 31 days")
elif(month in b):
    print(month," have 30 days")
else:
    print(month," have 28 days")
