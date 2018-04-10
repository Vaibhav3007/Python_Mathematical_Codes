#For LCM, it can never be less than given numbers.
#LCM is smallest number which gets completely divided by two/or given numbers


n1 = int(input("Enter first number- "))
n2 = int(input("Enter first number- "))

if n1>n2:
    maxx = n1
else:
    maxx = n2

while(1):
    if (maxx%n1 == 0 and maxx%n2 == 0):
        print(maxx)
        break
    maxx += 1


#Reason for starting loop from largest number is to reduce the number of iterations for second loop
    
