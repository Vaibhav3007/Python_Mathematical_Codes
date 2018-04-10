# checking a prime number

n = int(input('Enter a number : '))
div = 2

if n == 1:
    print("Number",n,"is neither Prime nor Composite")
elif n == 2:
    print("Number",n,"is Prime")
else:   
    while div < n:
        remain = n%div
        if remain == 0:
            print("Number",n,"is Composite")
            break
        div += 1
    if remain == 1:
        print("Number",n,"is Prime")

fac = [x for x in range(1,n+1) if n%x == 0]
print("Factors of",n,"are: ",fac)
