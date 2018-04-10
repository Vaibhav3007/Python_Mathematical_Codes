#HCF of two numbers

a = int(input("Enter 1st number- "))
b = int(input("Enter 2nd number- "))

maxx = max(a,b)
div = 2
check = 0

while div < maxx:
    if(a%div == 0 and b%div == 0):
        print("HCF or GCD of",a,"and",b,"is",div)
        check = 1
        break
    div += 1

if check == 0:
    print("HCF or GCD of",a,"and",b,"is",1)
