import collections
"""namedtuple"""
# Point = collections.namedtuple('Map', ['x', 'y',"z"])
# Player_Point = Point(10,10,10)
# print(Player_Point.x)
# print(Player_Point.y)
# print(Player_Point.z)
# print(type(Player_Point))
# print("all func:","\n".join(Player_Point.__dir__()))



"""deque"""
a = [i for i in range(100) if i % 2 == 0]
print(a)
for i in [i for i in range(200) if i % 3 == 0]:
    a.append(i)

print(sorted(set(a),reverse=True))
