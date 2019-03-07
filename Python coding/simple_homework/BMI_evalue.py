w=input('weight=')
h=input('high=')
weight=float(w)
high=float(h)
BMI=weight/(high*high)
print('BMI=',BMI)
if BMI<18.5:
    print('过轻')
elif BMI<25:
    print('正常')
elif BMI<28:
    print('过重')
elif BMI<32:
    print('肥胖')
else:
    print('过于肥胖')
