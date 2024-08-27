import time


def Logger(func):
    def wrapper(*args):
        t1=time.time()
        print(f"[info] Run in {func.__name__}")
        a=func()
        t2=time.time()
        Total_Time=t2-t1
        print(a)
        print("[info] Time {:0.4}".format(Total_Time))
        return a
    return wrapper

@Logger
def Demo():
    Total=0
    for i in range(100000):
        if i%10==0:
           Total+=i
    return Total


Demo()