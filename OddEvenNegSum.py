n = (input("Enter elements: "))
nums = [int(x) for x in n.split(" ")]

sum_e = 0
sum_o = 0
sum_n = 0

for i in nums:
    if i>0:  
        if i%2 == 0:
            sum_e = sum_e+i
        else:
            sum_o = sum_o+i
    else:
        sum_n = sum_n+i


print("Sum of odds =",sum_o)
print("Sum of evens =",sum_e)
print("Sum of negatives =",sum_n)
