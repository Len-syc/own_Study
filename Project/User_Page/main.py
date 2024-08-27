from functions import *

if __name__ == "__main__":
    logger = initLog()
    logged_in_user = None

    while True:
        print("""-----------System-----------
1. register
2. login
3. set_security_questions
4. forget_password
5. add_todo
6. update_todo
7. delete_todo
8. complete_todo
9. show_todos
10. logout
11. exit
-----------System-----------""")
        action = input("输入序号：")
        match action:
            case '1':
                user = input("请输入用户名: ")
                password = input("请输入密码: ")
                register(user, password)

            case '2':
                user = input("请输入用户名: ")
                password = input("请输入密码: ")
                if login(user, password):
                    logged_in_user = user

            case '3':
                if logged_in_user:
                    questions = {}
                    while True:
                        question = input("请输入安全问题(输入done结束): ")
                        if question == "done":
                            break
                        answer = input(f"请输入问题 '{question}' 的答案: ")
                        questions[question] = answer
                    set_security_questions(logged_in_user, **questions)
                else:
                    print("请先登录")

            case '4':
                user = input("请输入用户名: ")
                answers = {}
                while True:
                    question = input("请输入你设置的安全问题(输入done结束): ")
                    if question == "done":
                        break
                    answer = input(f"请输入问题 '{question}' 的答案: ")
                    answers[question] = answer
                forget_password(user, **answers)

            case '5':
                if logged_in_user:
                    todo = input("请输入要添加的TODO任务: ")
                    add_todo(logged_in_user, todo)
                else:
                    print("请先登录")

            case '6':
                if logged_in_user:
                    todo_index = int(input("请输入要更新的TODO索引: "))
                    new_todo = input("请输入新的TODO任务: ")
                    update_todo(logged_in_user, todo_index, new_todo)
                else:
                    print("请先登录")

            case '7':
                if logged_in_user:
                    todo_index = int(input("请输入要删除的TODO索引: "))
                    delete_todo(logged_in_user, todo_index)
                else:
                    print("请先登录")

            case '8':
                if logged_in_user:
                    todo_index = int(input("请输入要标记为完成的TODO索引: "))
                    complete_todo(logged_in_user, todo_index)
                else:
                    print("请先登录")

            case '9':
                if logged_in_user:
                    show_todos(logged_in_user)
                else:
                    print("请先登录")

            case '10':
                if logged_in_user:
                    print(f"{logged_in_user} 已注销")
                    logged_in_user = None
                else:
                    print("没有用户登录")

            case '11':
                print("退出程序")
                break

            case _:
                print("无效的操作，请重新选择")
