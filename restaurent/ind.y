
users = int(input("ENTER A YEAR"))
if(users%0==0 and users%100!=0) or (users%400==0):
    print("LEAP YEAR")
else:
    print("not a leap year")