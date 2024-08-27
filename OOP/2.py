# class Server():
#     def __init__(self,ip,port,version):
#         self.ip = ip
#         self.port = port
#         self.version = version
#     @property
#     def Get_Message(self):
#         print(self.ip,self.port,self.version)
#     @Get_Message.setter
#     def connect(self,ip):
#         if len(self.ip)>6:
#             print("ip Error")
#             raise ValueError
#         print("Connecting to " + self.ip + ":" + str(self.port))
#
# PS = Server("192.168.1.10",8080,1)
# PS.Get_Message()

#
# class Student:
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if 0 <= value <= 150:
#             self._age = value
#         else:
#             raise ValueError("Valid value must be in [0, 150]")
#
#
# s = Student()
# s.age = -27