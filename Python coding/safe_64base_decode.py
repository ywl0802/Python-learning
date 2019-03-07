import base64,re
def safe_base64_decode(s):#要求：去除解码后的等号‘=’
    le = len(s) % 4
    if le != 0:    # 这里说明缺了=
        s += (4 - le)*b'='
    print(s)
    return base64.b64decode(s)






# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
