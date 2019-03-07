import math
def quadratic(a,b,c):  #a*x^2+b*x+c=0的两个解
    x1=(-b+math.sqrt(b*b-4*a*c))/(-2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(-2*a)
    return x1,x2

x1,x2=quadratic(2,3,1)
print(x1,x2)