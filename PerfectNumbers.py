"""Perfect numbers are those whose factors (including 1) adds to itself"""



#n = int(input("Enter the number- "))

nums = [x for x in range(1,501)]
pn = []

for i in range(len(nums)):
    n = int(nums[i])
    fac = [x for x in range(1,n) if n%x==0]
    #print("Factors of",n,"are",fac)
    if sum(fac) == n:
        pn.append(n)
print("Perfect numbers between",nums[0],"and",nums[-1])
print(pn)
            
