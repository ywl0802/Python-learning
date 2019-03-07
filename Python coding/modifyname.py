def normalize(L):
    L=L[0].upper()+L[1:].lower()
    return L
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)