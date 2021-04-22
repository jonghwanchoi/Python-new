from urllib.parse import urlencode, unquote
import requests
import json

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
print("===== response json data start =====")
print(response)
print("===== response json data end =====")
print()

r_dict = json.loads(response.text)
r_list = r_dict.get("list")

result = {}
for item in r_list: 
    print("[테마 휴게소] : " + item.get("stdRestNm") + "\n[특징] : " + item.get("itemNm") + "\n[세부 설명] :\n" + item.get("detail")+"\n")
    
        
print("===== response dictionary(python object) data start =====")
print(result)
print("===== response dictionary(python object) end =====")
print()