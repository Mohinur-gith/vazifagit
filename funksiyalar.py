def xfunk(x):
    return lambda y: y **x
def find_value(f,x):
    print("x=",x,"f(x)=",f(x))
my_funk = lambda x: x * 2 + x
find_value(my_funk,0.5)  #x = 0.5 f(x)= 1.5
find_value(lambda x : 1/(x+2),2.0) # x = 2.0 f(x)= 0.25
z = 1 +((lambda x,y : (x +y)/3)(12,3)**2) # z = 26
print(xfunk(2)(3)) # 9
print(z)