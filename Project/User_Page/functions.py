# import json
# import hashlib
# from datetime import datetime
# from contextlib import contextmanager,closing
# import logging
# """
# TODO
# 1.注册
# 2.登录
# 3.忘记密码
# 4.登录完成之后展示TODO
# 5.增加,修改,删除TODO,已完成
# """
#
# # def Write_json(Value):
# #     with open("./User_Page.json",'w') as f:
# #         json.dump(Value,f)
# #         f.close()
# #     return True
# # def Check_json(type,Value):#["User"]["Password"]
# #     with open("./User_Page.json",'r') as f:
# #         # match Value:
# #         #     case "ID":
# #         #         for item in Json_list:
# #         #             if item.get("ID") == target_id:
# #         #                 return True
# #         #         return False
#
# def initLog():
#     logger = logging.getLogger('System')
#     logger.setLevel(logging.DEBUG)
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#
#
# """
# {"LenQin":{}}
# """
# DataBase = [{}]
# def find_id_index(target_id,dict_list=DataBase):
#     for index, item in enumerate(dict_list):
#         if item.get("id") == target_id:
#             return index
#     return -1
# def Login(User:str,Password:str):
#     try:
#         if User in DataBase:
#             if hashlib.md5(Password.encode()).hexdigest() + hashlib.sha1(User.encode()).hexdigest() == DataBase[find_id_index()]["password"]:
#                 return True
#             else:
#                 logging.error("密码错误")
#                 return False
#         elif User not in DataBase:
#             logging.error("用户不存在")
#             return False
#         else:
#             logging.error("Error")
#     except (ValueError,TypeError) as e:
#         logging.error("账号密码类型错误",e)
#
#
# def Register(User:str,Password:str):
#     try:
#         if User in DataBase:
#             logging.error("用户名已存在：",User)
#             return False
#         else:
#             DataBase[User]["Password"] = hashlib.md5(Password.encode()).hexdigest() + hashlib.sha1(User.encode()).hexdigest()
#             logging.info("创立成功！")
#     except (ValueError,TypeError) as e:
#         logging.error("账号密码类型错误",e)
#
#
# def SetSafe(User:str,**answer) ->str:
#     try:
#         for k in q.keys():
#             for v in q.values():
#                 DataBase[User][k] = v
#         else:
#             logging.error("Error")
#     except (ValueError,TypeError) as e:
#         logging.error("Error",e)
# def ForgetPassword(User:str,**q) -> str:
#     def get_all_keys(User,dict_list):
#         keys = set()
#     for item in [User][dict_list]:
#         keys.update(item.keys())
#     return keys
#     try:
#         if User in DataBase:
#             if




import hashlib
import logging
import json

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

def write_json(data):
    with open("./User_Page.json", 'w') as f:
        json.dump(data, f)
    return True

def read_json():
    try:
        with open("./User_Page.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

DataBase = read_json()

def find_id_index(target_id, dict_list=DataBase):
    for index, item in enumerate(dict_list):
        if item.get("id") == target_id:
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
        else:
            new_user = {
                "id": user,
                "password": hashlib.md5(password.encode()).hexdigest() + hashlib.sha1(user.encode()).hexdigest(),
                "todos": [],
                "security_questions": {}
            }
            DataBase.append(new_user)
            write_json(DataBase)
            logger.info("注册成功！")
            return True
    except (ValueError, TypeError) as e:
        logger.error("账号密码类型错误: %s", e)
        return False

def set_security_questions(user: str, **questions):
    try:
        index = find_id_index(user)
        if index != -1:
            DataBase[index]["security_questions"] = questions
            write_json(DataBase)
            logger.info("安全问题设置成功")
            return True
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("设置安全问题时出错: %s", e)
        return False

def forget_password(user: str, **answers):
    try:
        index = find_id_index(user)
        if index != -1:
            security_questions = DataBase[index].get("security_questions", {})
            if security_questions == answers:
                new_password = hashlib.md5("new_password".encode()).hexdigest() + hashlib.sha1(user.encode()).hexdigest()
                DataBase[index]["password"] = new_password
                write_json(DataBase)
                logger.info("密码已重置为 new_password")
                return True
            else:
                logger.error("安全问题答案错误")
                return False
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("重置密码时出错: %s", e)
        return False

def add_todo(user: str, todo: str):
    try:
        index = find_id_index(user)
        if index != -1:
            DataBase[index]["todos"].append({"task": todo, "completed": False})
            write_json(DataBase)
            logger.info("TODO 添加成功")
            return True
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("添加 TODO 时出错: %s", e)
        return False

def update_todo(user: str, todo_index: int, new_todo: str):
    try:
        index = find_id_index(user)
        if index != -1:
            if 0 <= todo_index < len(DataBase[index]["todos"]):
                DataBase[index]["todos"][todo_index]["task"] = new_todo
                write_json(DataBase)
                logger.info("TODO 更新成功")
                return True
            else:
                logger.error("TODO 索引无效")
                return False
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("更新 TODO 时出错: %s", e)
        return False

def delete_todo(user: str, todo_index: int):
    try:
        index = find_id_index(user)
        if index != -1:
            if 0 <= todo_index < len(DataBase[index]["todos"]):
                del DataBase[index]["todos"][todo_index]
                write_json(DataBase)
                logger.info("TODO 删除成功")
                return True
            else:
                logger.error("TODO 索引无效")
                return False
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("删除 TODO 时出错: %s", e)
        return False

def complete_todo(user: str, todo_index: int):
    try:
        index = find_id_index(user)
        if index != -1:
            if 0 <= todo_index < len(DataBase[index]["todos"]):
                DataBase[index]["todos"][todo_index]["completed"] = True
                write_json(DataBase)
                logger.info("TODO 标记为已完成")
                return True
            else:
                logger.error("TODO 索引无效")
                return False
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("标记 TODO 完成时出错: %s", e)
        return False
def show_todos(user: str):
    try:
        index = find_id_index(user)
        if index != -1:
            todos = DataBase[index].get("todos", [])
            if todos:
                for i, todo in enumerate(todos):
                    status = "完成" if todo["completed"] else "未完成"
                    print(f"{i}. {todo['task']} - {status}")
            else:
                print("没有 TODO 任务")
            return True
        else:
            logger.error("用户不存在")
            return False
    except (ValueError, TypeError) as e:
        logger.error("显示 TODO 时出错: %s", e)
        return False
