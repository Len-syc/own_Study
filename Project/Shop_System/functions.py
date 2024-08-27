import json
import hashlib
import logging

# 初始化日志
def init_log():
    logger = logging.getLogger('ShopSystem')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = init_log()

# 数据库初始化
Users = []
Products = []

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return True

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

Users = read_json("Users.json")
Products = read_json("Products.json")

def find_user_index(username, user_list=Users):
    for index, item in enumerate(user_list):
        if item.get("username") == username:
            return index
    return -1

def find_product_index(product_name, product_list=Products):
    for index, item in enumerate(product_list):
        if item.get("name") == product_name:
            return index
    return -1

def register(username: str, password: str, role: str = "user"):
    pass  # 实现注册功能

def login(username: str, password: str):
    pass  # 实现登录功能

def add_product(name: str, price: float, stock: int):
    pass  # 实现添加商品功能（管理员功能）

def view_products():
    pass  # 实现查看商品列表功能

def add_to_cart(username: str, product_name: str, quantity: int):
    pass  # 实现添加商品到购物车功能

def view_cart(username: str):
    pass  # 实现查看购物车功能

def remove_from_cart(username: str, product_name: str):
    pass  # 实现从购物车中移除商品功能

def checkout(username: str):
    pass  # 实现结账功能

if __name__ == "__main__":
    logged_in_user = None

    while True:
        if logged_in_user:
            print(f"欢迎, {logged_in_user}!")
            print("""-----------Shop System-----------
1. view_products
2. add_to_cart
3. view_cart
4. remove_from_cart
5. checkout
6. add_product (Admin only)
7. logout
8. exit
-----------Shop System-----------""")
        else:
            print("""-----------Shop System-----------
1. register
2. login
3. exit
-----------Shop System-----------""")

        action = input("输入序号：")
        if logged_in_user:
            match action:
                case '1':
                    view_products()

                case '2':
                    product_name = input("请输入商品名称: ")
                    quantity = int(input("请输入数量: "))
                    add_to_cart(logged_in_user, product_name, quantity)

                case '3':
                    view_cart(logged_in_user)

                case '4':
                    product_name = input("请输入要移除的商品名称: ")
                    remove_from_cart(logged_in_user, product_name)

                case '5':
                    checkout(logged_in_user)

                case '6':
                    user_index = find_user_index(logged_in_user)
                    if user_index != -1 and Users[user_index]["role"] == "admin":
                        name = input("请输入商品名称: ")
                        price = float(input("请输入商品价格: "))
                        stock = int(input("请输入商品库存: "))
                        add_product(name, price, stock)
                    else:
                        print("只有管理员可以添加商品")

                case '7':
                    print(f"{logged_in_user} 已注销")
                    logged_in_user = None

                case '8':
                    print("退出程序")
                    break

                case _:
                    print("无效的操作，请重新选择")

        else:
            match action:
                case '1':
                    username = input("请输入用户名: ")
                    password = input("请输入密码: ")
                    role = input("请输入角色 (user 或 admin): ")
                    register(username, password, role)

                case '2':
                    username = input("请输入用户名: ")
                    password = input("请输入密码: ")
                    if login(username, password):
                        logged_in_user = username

                case '3':
                    print("退出程序")
                    break

                case _:
                    print("无效的操作，请重新选择")
