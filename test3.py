import sqlite3
import pandas as pd

con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")
cur = con.cursor()

cur.execute("SELECT * FROM testTable")
rows = cur.fetchall() # 데이터 전체 읽어오기 
#이외도 fetchone()-한 줄만 읽기, fetchmany(size=x)-x줄 읽기 메서드들이 있다.
cols = [column[0] for column in cur.description]
data_df = pd.DataFrame.from_records(data = rows, columns = cols)

con.commit()
con.close()

print(data_df)