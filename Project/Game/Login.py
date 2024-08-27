import hashlib
import json
import logging

def initLog():
    logger = logging.getLogger('System')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
logger = initLog()
# 数据库初始化
DataBase = []
#------------------json-----------------------#
def write_json(data):
    with open("./DataBase/User_Data.json", 'w') as f:
        json.dump(data, f)
    return True

def read_json():
    try:
        with open("./DataBase/User_Data.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_ini(Model):
    try:
        match Model:
            case 'UID':
                with open("./DataBase/ini.json", 'r') as f:
                    data = json.load(f)
                    return data[0]
    except FileNotFoundError:
        return {"UID": 1}

def write_uid(uid_data):
    with open("./DataBase/ini.json", 'w') as f:
        json.dump([uid_data], f)
#------------------json-----------------------#

DataBase = read_json()

def find_id_index(target_id, dict_list=DataBase):
    for index, item in enumerate(dict_list):
        if item.get("name") == target_id:
            return index
    return -1

def login(user: str, password: str):
    try:
        index = find_id_index(user)
        if index != -1:
            stored_password = DataBase[index].get("password")
            input_password = hashlib.md5(password.encode()).hexdigest() + hashlib.sha1(user.encode()).hexdigest()
            if stored_password == input_password:
                logger.info("登录成功")
                return True
            else:
                logger.error("密码错误")
                return False
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("账号密码类型错误: %s", e)
        return False

def register(user: str, password: str):
    try:
        index = find_id_index(user)
        if index != -1:
            logger.error("用户名已存在: %s", user)
            return False

        uid_data = read_ini("UID")
        UidCount = uid_data["UID"]
        new_user = {
            "uid": UidCount,
            "name": user,
            "password": hashlib.md5(password.encode()).hexdigest() + hashlib.sha1(user.encode()).hexdigest()
        }
        DataBase.append(new_user)
        write_json(DataBase)
        uid_data["UID"] = UidCount+1
        write_uid(uid_data)
        logger.info("注册成功！")
        return True
    except (ValueError, TypeError) as e:
        logger.error("账号密码类型错误: %s", e)
        return False