l = int(input("Input lower range- "))
u = int(input("Input upper range- "))

nums = list(range(l,u+1,1))
print("Numbers between",l,"and",u,"divisible by 7 and multiple of 5 are ",end=">>>")
for i in nums:
    if (i%7 == 0) & (i%5 == 0):
        print(i,end=" ")


