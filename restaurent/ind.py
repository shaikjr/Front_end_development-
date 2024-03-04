
users = int(input("enter a year"))
if(users%4==0 and users%100!=0) or (users%400==0):
    print("leap year")
else:
    print("not leap year")