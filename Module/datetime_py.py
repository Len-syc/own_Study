from datetime import datetime

# 创建时间函数
def CreatTime(year=1970, month=1, day=1, hour=0, minute=0, second=0):
    return datetime(year, month, day, hour, minute, second)

print(CreatTime())
print(datetime.now())
print(datetime.timestamp(datetime.now()))


print(datetime.fromtimestamp(9999999999))
print(datetime.fromtimestamp(1722434836.905595))
