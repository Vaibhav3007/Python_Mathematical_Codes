# Strong number - 145 as 1!+4!+5! = 145

def factorial(x):
    if x == 1 or x == 0:
        fact = 1
    else:    
        fact = 1
        for i in range(1,x+1):
            fact = fact*i
    return fact
    
n = int(input("Enter a number: "))

sum_f = 0
temp = n

while n > 0:
    i = n%10
    n = n//10
    fact = factorial(i)
    sum_f = sum_f + fact

if sum_f == temp:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
        
