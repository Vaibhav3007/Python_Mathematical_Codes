p = float(input("Enter principal amount- "))
r = float(input("Enter rate of interest- "))
t = float(input("Enter time period in years- "))

si = (p*r*t)/100
a = p+si

print("Simple Interest for ",p," for ",t," years,calculated @ ",r,"% per annum is ",si,sep="")
print("Total amount-",a)
