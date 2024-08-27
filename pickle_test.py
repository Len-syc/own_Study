import pickle
import json
Dict = {"User":"LenQin","pwd":"1234"}
with open('test.txt', 'wb') as f:
    f.write(pickle.dumps(Dict))
    f.close()
##序列化写入文件
with open('test.txt', 'rb') as f:
    Dict = pickle.loads(f.read())
    f.close()
##反序列化
# d = dict(name='Bob', age=20, score=88)
# with open('message.json', 'w') as f:
#     f.write(json.dumps(d))
#     f.close()
with open('config.json', 'r') as f:
    d = json.load(f)
    f.close()
    print(d)