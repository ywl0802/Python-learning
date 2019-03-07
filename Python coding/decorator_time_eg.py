import functools,time

def log(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start = time.time()
        result = fn(*args,**kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end - start) *1000))
        return result
    return wrapper
    
@log
def fast(x, y):
    time.sleep(0.0012)
    print('func fast')
    return x + y;

@log
def slow(x, y, z):
    time.sleep(0.1234)
    print('func slow')
    return x*y*z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

