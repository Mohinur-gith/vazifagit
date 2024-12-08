'''from math import *
x=int(input("x="))
y=int(input("y="))
print(fabs(x)<=1)==(fabs(y)>=1)
print((x*x+y*y<=4)== (y<=x))'''
n=int(input("n="))
m=int(input("m="))
#Yig'indi uchun
s=0
# Qadamlarni sanash uchun
i=2
while i<=n:
    p=1
    j=3
    while j<=m:
        p*=float(i*i)/(j)
        j+=1
    s+=p
    i+=1
print("s=",s)
sum=0
n=int(input("n= "))
i=1
while i<=n:
    sum=sum+i
    i+=1
print("summa (1+...+n) =",sum)