import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3  = "", "", ""  # id, name, mobile
sql=""
i,j = 0,0
familyNames=list("김이송박최정강조이장임한김고전홍박이김이") #이름 20개
firstNames = list("태희영애혜교예진정현윤희수연가인수지미주은하채영성령아라인화진영초롱지은사랑주은")

## 메인 코드 부분 ##
con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
cur = con.cursor()

while (i<len(familyNames)) :
    data1 = input("사용자ID ==> ")
    if data1 == "" :
         break;
    data2 = familyNames[i]+firstNames[j]+firstNames[j+1]
    data3 = input("전화번호==> ")
    sql = "INSERT INTO Student VALUES("  +  data1  +  ",'"  +  data2  +  "','"  +  data3  + "')"
    cur.execute(sql)
    i+=1
    j+=2
    
con.commit()
con.close()