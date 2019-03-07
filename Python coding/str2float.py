from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    return reduce(fn,map(int,s.split('.')[0]))+reduce(fn,map(int,s.split('.')[1]))/pow(10,len(s.split('.')[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')