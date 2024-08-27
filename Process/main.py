from threading import Thread
import time
def timer(mode):
    def wrapper(func):
        def deco(*args, **kw):
            t1=time.time()
            func(*args, **kw)
            t2=time.time()
            cost_time = t2-t1
            print("{}-{}花费时间：{}秒".format(mode, type,cost_time))
        return deco
    return wrapper
@timer("多进程")
def Count(a:int,b:int):
    for i in range(50000):
        print(i,"：",(a+b)**2+i)

quest1 = Thread(target=Count, args=(10, 10))
quest1.start()


