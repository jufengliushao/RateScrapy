import json
from ..Models.RateHLModel import HLModel

def settingDataFromJSON(json):
    datas = []
    for dic in json["records"]:
        print(dic)