from contextlib import contextmanager,closing
from urllib.request import urlopen

""""""

#yield 用法
def Count(Max):
    _a = 0
    while _a < Max:
        _a += 1
        yield _a
def AllCount():
    c = Count(10)
    try:
        while True:
            print(next(c))
    except StopIteration:
        print("Over")


#@contextmanager
@contextmanager
def Resp(name):
    print(name)
    yield "i am return to the [with] code ep:How to use me? :add code to the with,ep: with Resp() as Value,then print it"
    print("Goodbye world")
#如果没加 as Value 则 yield 后面的字符串就不会返回到with上下文中
with Resp("Hello World") as Value:
    print(Value)
    print("TODO")



# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)
