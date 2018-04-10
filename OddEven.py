n = input("Enter elements: ")

num = [int(x) for x in n.split(" ")]

even = []
odd = []

for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Biggest even num =",max(even))

print("Biggest even odd =",max(odd))

