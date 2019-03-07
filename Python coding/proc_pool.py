from multiprocessing import Pool 
import os, time, random
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time() #返回当前的时间戳
    time.sleep(random.random()*3)#推迟执行的秒数
    end = time.time()
    print('Task %s runs %0.2f scconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #同时跑4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) #spply_async异步非阻塞 不用等待当前进程执行完毕
    print('Waiting for all subprocesses done...')
    p.close()#子进程关闭
    p.join()#父进程等子进程完毕后继续执行
    print('All subprocesses done.')
