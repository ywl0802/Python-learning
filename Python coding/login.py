# -*- coding: utf-8 -*-
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    def cal_md5(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        a = md5.hexdigest()
        return a
    for i,m in db.items():          #对dic的一个应用，每个key和value是对应的，找到符合条件的key，
        if user==i:                 #然后就可以对相应的value进行处理,每次取出的是K:V
            b=cal_md5(password)     #如果是 for i in db.items() 那么取出的是什么呢？value吗？
            if b==m:
                return True
                print('ok')
            else:
                return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')