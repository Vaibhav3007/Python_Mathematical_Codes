#Number range without loop

def range_no_loop(start,end):
    if start <= end:
        print(start)
        range_no_loop(start+1,end)


start = int(input("Enter starting number- "))
end = int(input("Enter ending number- "))

range_no_loop(start,end)


'''    
def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
upper=int(input("Enter upper limit: "))
printno(upper)
'''
