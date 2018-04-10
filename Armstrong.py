n = input("Enter a Number - ")
x=0
a = []
temp = int(n)

for i in n:
    x = int(i)
    a.append(x**3)
    
if sum(a) == temp:
    print(temp,"is Armstrong")
else:
    print(temp,"is not Armstrong")





#371 is armstrong
#3**3+7**3+1**3 = 371
