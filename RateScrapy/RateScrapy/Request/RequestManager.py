import urllib
import json

def request_rmyh_hl():
    response = request_get_url_datas('http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/ccpr.json', {})
    responseJS = json.loads(response)
    print(responseJS)

def request_get_url_datas(url, paraDic):
    if len(url) < 5:
        return
    preuqets_url = request_get_url_param(url, paraDic)
    request = urllib.request.urlopen(
                request_get_url_param(url, paraDic),
                data=None,
                timeout=10)
    responseInfo = request.read().decode()
    return responseInfo


def request_get_url_param(url, param):
    if len(param) == 0:
        return url
    url += "?"
    str = ""
    for key, value in param.items():
        str = str + key + "=" + value + "&"
    url += str
    return url[0:len(url-1)]