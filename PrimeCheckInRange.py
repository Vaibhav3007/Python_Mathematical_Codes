# checking a prime number in range

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))

nums = [x for x in range(n1,n2+1)]
prime = []

for n in nums:
    if n == 1:
        pass
    elif n == 2:
        prime.append(n)
    else:
        div = 2
        while div < n:
            remain = n%div
            if remain == 0:
                break
            div += 1
        if remain == 1:
            prime.append(n)

print("Prime numbers between",n1,"&",n2,"are",prime)
    
        
