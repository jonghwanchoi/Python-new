import sqlite3

con,cur = "",""
def DBread():
    con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM Test")
    rows = cur.fetchall() # 데이터 전체 읽어오기 
    con.commit()
    con.close()
  
    return rows