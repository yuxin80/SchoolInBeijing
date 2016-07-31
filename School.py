from ConstantsAndEnum import *
import uuid
import jsonpickle
import json

class school:
    def __init__(self):
        self.Dist = District.Other
        self.SchoolType = ClassType.JuniorSchool
        self.Id = uuid._UuidCreate()
        self.Name = ''
        self.ZhaoShengJianzhang = ''

    def __init__(self, name:str, dist:District, classtype:ClassType):
        self.Dist = dist
        self.SchoolType = classtype
        self.Id = uuid._UuidCreate()
        self.Name = name
        self.ZhaoShengJianzhang = ''

    def to_JSON(self):
        return json.dumps(json.loads(jsonpickle.encode(self)),sort_keys=True, indent=4)
