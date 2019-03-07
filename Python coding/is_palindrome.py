def is_palindrome(n):
    s=str(n)
    i=0
    x=0
    while i<=int(len(s)/2):
        if s[i]==s[-i-1]:
            x=x
        else:
            x=x+1
        i=i+1
    if x==0:
        return True
    else:
        return False

# 测试:
output = filter(is_palindrome, range(1, 1000000))
print('1~1000000:', list(output))
