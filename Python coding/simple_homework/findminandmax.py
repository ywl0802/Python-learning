def findMinAndMax(L):
    a=len(L)
    if a==0:
        return(None,None)
    else:
        x=L[0]
        y=L[0]
        for value in L:
            if value>=x:
                x=value
            if value<=y:
                y=value
        return(y,x) 

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')