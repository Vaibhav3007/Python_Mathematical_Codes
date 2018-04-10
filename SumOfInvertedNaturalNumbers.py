n = int(input("Enter the terms to be calculated - "))
i = 2
summ = 1

for i in range(1,n+1):
    summ = summ+(1/i)

print("%0.4f" %summ)
