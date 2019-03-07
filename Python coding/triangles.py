def triangles():
    L1=[1]
    L2=[1,1]
    yield L1
    L1=L2[:]
    yield L1
    while True :
        L1=L2[:]
        L2.append(1)
        for s in range(1,len(L2)-1):
            L2[s]=L1[s]+L1[s-1]
        L1=L2[:]
        yield L1
        

i = 0
results = []        
for t in triangles():
    print(t)
    results.append(t)
    i = i + 1
    if i == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')       

