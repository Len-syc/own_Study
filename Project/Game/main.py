from Login import *
User_Name = "null"
def LoginPage():
    try:
        while True:
            global User_Name
            print("""
        ------------GenSha Game------------
        1.登录
        2.注册
        ------------GenSha Game------------
        """)
            Select = int(input(""))
            match Select:
                case 1:
                    User_Name = input("User:")
                    Password = input("Password:")
                    login(User_Name,Password)
                case 2:
                    User_Name = input("User:")
                    Password = input("Password:")
                    register(User_Name,Password)
            return True
    except Exception as e:
        logging.error(e)
        return False



def GamePage():
    try:
        while True:
            print(f"Welcome to the Game{User_Name}")
            print("""
            ------------主页------------
            1.角色
            2.背包
            3.挑战
            4.
            ------------主页------------
            """)