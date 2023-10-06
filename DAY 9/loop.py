#################################################### LOOP ###########################################################
# to execute statements repeatedly
# 1. For
# 2. while
# 3. nested loop

# while loop
# where i is iteration variable, which decide iteration values

# # 1,3,5,7,9,11
i = 1
while(i<=11):
    print(i)
    i = i+2

# 5,10,15,20,25,30
i = 5
while(i<=30):
    print(i, end=" ")
    i = i+5

# 1,2,4,7,11,16,22

i = 1
k = 1
while(i<=36):
    print (i)
    i = i+k
    k = k+1

# 2,5,10,17,26,37

i = 2
k = 3
while(i<=37):
    print (i)
    i = i+k
    k = k+2

# in between 100 and 500 how many even numbers are there with total number of count

i = 100
count = 0
while(i<=500):
    if(i%2==0):
        count = count + 1
        print (i)
        i = i+2
print(count)



