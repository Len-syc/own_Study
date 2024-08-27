"""lambda"""
# b= int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# a=(lambda x,y:x+y)
# print(a(b,c))
# print((lambda a,b:a*2 if a>b else b)(4,2))

"""map"""
# List = [i for i in range(100)]
# a=map(lambda x: x ** 2, List)
# print(type(a))
# for i in range(5):
#     print(next(a))
#


"""filter"""

List = [i for i in range(100)]
List= filter(lambda x: x%2==0, List)
for i in List:
    print(i)
    # raise ZeroDivisionError
print(isinstance(List,list))
