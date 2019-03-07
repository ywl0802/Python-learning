from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
#.getpid()取得进程识别码 

#父进程描述
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) 
    #子进程创建，target指向执行函数，args为参数
    print('Child process will start.')
    p.start()#子进程启动
    p.join()#子进程结束后再继续往下运行
    print('Child process end.')
