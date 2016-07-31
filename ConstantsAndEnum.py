from enum import Enum

class ClassType(Enum):
    JuniorSchool=1
    MiddleSchool=2
    HighSchool=3

class District(Enum):
    ChaoYang =1
    HaiDian = 2
    XiCheng = 3
    DongCheng = 4
    Other = 5

DistrictMap={"海淀":District.HaiDian, "朝阳":District.ChaoYang, "西城":District.XiCheng,"东城":District.DongCheng}
