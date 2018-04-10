# Strong number - 145 as 1!+4!+5! = 145

def factorial(x):
    if x == 1 or x == 0:
        fact = 1
    else:    
        fact = 1
        for i in range(1,x+1):
            fact = fact*i
    return fact
    
#n = int(input("Enter a number: "))
num = [k for k in range(1,100001)]
sum_f = 0
SN = []

for z in range(len(num)):
    n = num[z]
    temp = n
    sum_f = 0
    while n > 0:
        i = n%10
        n = n//10
        sum_f = sum_f + factorial(i)
    if sum_f == temp:
        SN.append(temp)

print("Strong numbers between",num[0],"and",num[-1],"are\n",SN)
