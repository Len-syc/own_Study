# import time
# def isNumber(num):
#     if num%2 == 0:
#         return True
#     else:
#         return False
# def Deco(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return result
#     return wrapper
#
# def ex():
#     result=0
#     for i in range(1000):
#         if isNumber(i):
#             result+=1
#     return result
#
#


#
# def apply(func):
#     def wrapper(self,*args, **kwargs):
#         result =  func(self,*args, **kwargs)
#         if self.lv == 100:
#             self.HP +=20
#             self.defense += 20
#         print(self.ID)
#         print(self.HP)
#         print(self.defense)
#         print(self.lv)
#         return float(self.HP),float(self.defense)
#     return wrapper
#
#
# class character (object):
#     def __init__(self,ID,lv,HP,defense):
#         self.ID = ID
#         self.lv = lv
#         self.HP = HP
#         self.defense = defense
#     @apply
#     def upgrade(self):
#         self.HP += 0.5
#         self.lv +=1
#         self.defense += 0.5
#         if self.lv %10 == 0:
#             self.HP += 10
#             self.defense += 10
#         return self.HP,self.lv,self.defense
#
#
# LenQin = character('LenQin',10,100,100)
# for _ in range(101):
#     LenQin.upgrade()









# a = input("")
# number = a or -1
# print(number) 






"""
*用法
1.打包 list,dict,tuple,set
2.解包
"""
# 1.list
a = [1,2,3,4]
b = [5,6,7,8]
c = [*a,*b]
# -> list [1,2,3,4,5,6,7,8]
# 1.1.Dict
a_dict = {
	"name":"bob",
	"age":10
}
b_dict = {
	"city":"ShangHai",
	"detail":"None"
}
c_dict = {**a_dict,**b_dict}#tips 如果用*，只会传key
#->{'name': 'bob', 'age': 10, 'city': 'ShangHai', 'detail': 'None'}
d_dict = [i for i in [*a_dict,*b_dict]]
# 看实际情况,如果是需要好几个dict的key,就使用这个
#-> ['name', 'age', 'city', 'detail']
c_dict = [i for i in a_dict.keys()]
# 单个 -> ['name', 'age']

#1.2 tuple
a_tuple = (1,2,3)
b_tuple = (4,5,6)
c_tuple = (*a_tuple,*b_tuple)
# -> (1, 2, 3, 4, 5, 6)
#1.3 set
a_set = {1,2,3}
b_set = {4,5,6}
c_set = {*a_set,*b_set}
# -> {1, 2, 3, 4, 5, 6}

#2.0
def Count(*a):
	""" a只能接收一个参数.这里的一个参数是：比如列表a也是一个参数，但a里面可以有很多参数
		Count([10,20],[10,20]) -> Error
		*a可以接收多个参数
		Count(1,2,3,4,5,6,7) ->1,2,3,4,5,6,7
		"""
	for i in a:
		print(f"{i}")

def profile(name,age):
	print(f"key：{name},Value：{age}")
ep = {
	"name":"bob",
	"age":18,
}
profile(**ep)


def show(**kwarges):
	for k,v in kwarges.items():
		print(f"key:{k},value:{v}")

show(a=1,b=1,c=2)


