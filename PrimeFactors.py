n = int(input("Enter the number- "))

fac = [x for x in range(2,n) if n%x==0]
pf = []

print("Factors of",n,"are",fac)

for i in range(len(fac)):
    for j in range (2,fac[i]):
        if fac[i]%j == 0:
            break
    else:
           pf.append(fac[i])
    
        
print("Prime factors of",n,"are",pf)
