import serial
import sqlite3

cur,con = None, None
data = ""
sql = ""

port = serial.Serial('COM5','9600') # 포트 연결

con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
cur = con.cursor()

while True :
    try:
        data = port.readline()
        strData = data[:-2].decode() #바이트 단위를 string으로 변환(-2는 \r\n을 제거하기 위함)
        sql = "INSERT INTO Test VALUES('" + strData + "')"
        cur.execute(sql)
        con.commit()
    except KeyboardInterrupt:
        break; 

port.close()
con.close()