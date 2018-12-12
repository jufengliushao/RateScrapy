import json
from ..Models.RateHLModel import HLModel

def settingDataFromJSON(json):
    datas = []
    ts = json["head"]["ts"]
    update = json["data"]["lastDate"]
    for dic in json["records"]:
        model = HLModel(
                price=dic["price"],
                bp=dic["bp"],
                vrtName=dic["vrtName"],
                vrtEName=dic["vrtEName"],
                foreignCName=dic["foreignCName"],
                bpDouble=dic["bpDouble"],
                bannerPic=dic["bannerPic"],
                vrtCode=dic["vrtCode"],
                ts=ts,
                update=update)
        datas.append(model)
    return datas

