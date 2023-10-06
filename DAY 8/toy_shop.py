print("Welcome To Toy Shop")
print("1. Battery based top - $250 (10% for $1000 and above) \n2. Key based top - $40 (5% for $100 and above) \n3. Eletric based top - $150 (10% for $500 and above)")
purchase = int(input("Please select your toy :- "))
if(purchase==1):
    quanity = int(input("Please select your quanity :- "))
    amount = quanity*250
    if(amount >= 1000):
        percentage = amount/100
        discount = percentage*10
        total = amount-discount
        print("$",total)
    else:
        print("$",amount)
elif(purchase==2):
    quanity = int(input("Please select your quanity :- "))
    amount = quanity*40
    if(amount >= 100):
        percentage = amount/100
        discount = percentage*5
        total = amount-discount
        print("$",total)
    else:
        print("$",amount)
elif(purchase==3):
    quanity = int(input("Please select your quanity :- "))
    amount = quanity*150
    if(amount >= 500):
        percentage = amount/100
        discount = percentage*10
        total = amount-discount
        print("$",total)
    else:
        print("$",amount)
else:
    print("Please enter a valid input")
print("Thank You")