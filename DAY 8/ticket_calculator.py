print("Welcome To Public Transportation")
ticket = int(input("Enter the distance you have travelled :- "))
if(ticket >= 1 and  ticket <= 50):
    charge = ticket*8
    print("Your charge for",ticket,"is $",charge)
elif(ticket >= 51 and ticket <= 100):
    charge = ticket*10
    print("Your charge for",ticket,"Km is $",charge)
else:
    print("Please enter a valid input")
print("Thank You")