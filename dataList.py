from urllib.parse import urlencode, unquote
from restArea import Rest
import requests
import json

def getData():
    url = "http://data.ex.co.kr/openapi/restinfo/restThemeList"
    queryString = "?" + urlencode(
        {
            "key" : "test",
            "type" : "json",
            "pageNo"    : "1",
            "numOfRows" : "10"
        }
    )   

    response = requests.get(url + queryString)
    r_dict = json.loads(response.text)
    r_list = r_dict.get("list")

#----------기존 실습 코드에서 추가--------------
    list = []
    for i in r_list:
        m = Rest(
            i['stdRestNm'], 
            i['itemNm'],
            i['detail']
        )
        list.append(m)
#----------------------------------------------
    return list