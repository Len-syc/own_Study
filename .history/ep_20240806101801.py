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






# *用法
print(10*2)
print("10"*2)
a = [1,2,3,4]
b = [5,6,7,8]
c = [*a,*b]
print("\n".join(*c))