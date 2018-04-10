date = input("Enter a date in dd/mm/yyyy: ")
dd,mm,yyyy = date.split("/")

dd=int(dd)
mm=int(mm)
yyyy=int(yyyy)

#print(dd,mm,yyyy)

if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max_date = 31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    max_date = 30
elif (mm==2 and yyyy%4 == 0):
    max_date = 29
else:
    max_date = 28

if (yyyy<1000 or yyyy>9999):
    print("Invalid Date")
elif (mm<1 or mm>12):
    print("Invalid Date")
elif (dd<1 or dd>max_date):
    print("Invalid Date")
elif (dd==max_date and mm!=12):
    dd=1
    mm=mm+1
    print("Next Date is: ",dd,"/",mm,"/",yyyy,sep="")
elif (dd==max_date and mm==12):
    dd=1
    mm=1
    yyyy=yyyy+1
    print("Next Date is: ",dd,"/",mm,"/",yyyy,sep="")
else:
    dd=dd+1
    print("Next Date is: ",dd,"/",mm,"/",yyyy,sep="")
