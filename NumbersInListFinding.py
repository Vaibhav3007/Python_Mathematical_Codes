# numbers in a list

import random

nums = []

for i in range(0,51):
    nums.append(random.randrange(1,11))

#print(nums)

n = int(input("Enter a number between 1 to 10: "))
count = 0

for x in nums:
    if x == n:
        count = count+1

print("The number",n,"appears",count,"times in the list")
