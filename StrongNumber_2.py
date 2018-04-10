def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact
 
 
for n in range(1, 1000000):
    tmp = n
    summ = 0
    while tmp != 0:
        reminder = tmp % 10
        summ = summ + factorial(reminder)
        tmp //= 10
    if summ == n:
        print(n)
