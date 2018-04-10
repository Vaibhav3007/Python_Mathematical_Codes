
num = [z for z in range(100,2000)]
final = []

for k in range(len(num)):
    n=str(num[k])

    x=0
    a = []
    temp = int(n)

    for i in n:
        x = int(i)
        a.append(x**len(n))
    
    if sum(a) == temp:
        final.append(temp)

print(final)


#371 is armstrong
#3**3+7**3+1**3 = 371
