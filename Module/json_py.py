import json
"""dump"""
def Dump_Json():
    NameList = ["jon","son","tom","h"]
    data = {k:v for k,v in enumerate(NameList,start=1)}
    data2 = [
        {"User":[{"id":1,"name":"bob","code":"10","langua":["python","javascript"]}],},
        {"User":[{"id":2,"name":"tom","code":"12","langua":["go","java"]}],},
    ]

    with open("./message.json","w") as f:
        json.dump(data2,f,indent=2)
        f.close()
"""load"""
def Load_Json():
    with open('./message.json', 'r') as file:
        data = json.load(file)
    # 输出读取的数据
    print("Users Data:")
    for user_data in data:
        user = user_data['User'][0]  # 获取 User 列表中的第一个用户信息字典
        print(user)
        print(f"ID: {user['id']}")
        print(f"Name: {user['name']}")
        print(f"Code: {user['code']}")
        print(f"Languages: {','.join(user['langua'])}")  # 将编程语言列表连接成逗号分隔的字符串
        print("-" * 20)
Load_Json()