from functools import reduce
def prod(L):
    def multi(x,y):
        return x*y
    p=reduce(multi,L)
    return p

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')