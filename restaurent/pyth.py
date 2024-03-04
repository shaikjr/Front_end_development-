
for i in range(1,5):
    print("* "*i)
    
a=42
b = type(str(a))
print(b)

c="123"
d = type(int(c))
print(d)

g= 3.14
e=print(type(int(g)))
print(e)


h="5.5"
f = print(type(float(h)))
print(f)


k = 100
s = print(type(bool(k)))
print(s)

t = True
e=print(type(int(t)))
print(e)


i = True
p=print(type(str(i)))
print(p)


x= "The future is bright."
print(x[::-1])


user = int(input("ENTER A NUMBER"))
if(user%2==0):
    print("even")
else:
    print("odd")
    
    
use = int(input("ENTER A NUMBER"))
use2 =int(input("ENTER A NUMBER"))
if(use>use2):
    print(use)
else:
    print(use2)
    
us = input("ENTER A LETTER")
vowels = "a,e,i,o,u"
if us in vowels:
    print(us,"is a vowel")
else:
    print(us,"is not a vowel")
    
mu = int(input("enter a year"))
if(mu %4==0 and mu%100!=0) or (mu%400 == 0):
    print("leap year")
else:
    print("not leap year")
    
    
    
users = int(input("ENTER A YEAR"))
if(users%0==0 and users%100!=0) or (users%400==0):
    print("LEAP YEAR")
else:
    print("not a leap year")