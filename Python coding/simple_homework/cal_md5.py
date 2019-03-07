import hashlib
def cal_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    a = md5.hexdigest()
    return a



b =  cal_md5('123456')
print(b)