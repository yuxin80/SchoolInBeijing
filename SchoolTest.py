import School
from ConstantsAndEnum import *
import jsonpickle

s = School.school("朝阳一小",District.ChaoYang,ClassType.JuniorSchool)
# s = School.school()
jsonStr = s.to_JSON()

print(jsonStr)

s1 = jsonpickle.decode(jsonStr)

assert s1.Name == s.Name
assert s1.SchoolType == s.SchoolType

print(s1.Name)
print(s.Name)
