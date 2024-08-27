"""list"""
# [a if a %2 ==0 else "不是偶数" for a in range(1,11)]
# [item for item in range(100) if item %2 == 0]


"""dict"""
# old_student_score_info = {
#     "Jack": {
#         "chinese": 87,
#         "math": 92,
#         "english": 78
#     },
#     "Tom": {
#         "chinese": 92,
#         "math": 100,
#         "english": 89
#     }
# }
# new_student_score_info = {name: scores for name, scores in old_student_score_info.items() if scores["math"] == 100}
# # new_student_score_info2 = {key: value for key, value in old_student_score_info.values() if value == 100}
# print(new_student_score_info)
namelist = ["hello","worldd"]
NewList=[a for a in range(1,100) if a % 2 == 0]
# print({k:len(k) for k in namelist if len(k)>5})