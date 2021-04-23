import sqlite3
from tkinter import *
from tkinter import messagebox
i,j = 0,0

## 함수 선언 부분
def insertData() :
    global i,j
    con, cur = None, None
    data1, data2, data3 = "", "", ""
    sql=""

    con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()

    data1 = edt1.get()
    if(i<len(familyNames)) : 
        data2 = familyNames[i]+firstNames[j]+firstNames[j+1]
    else :
        data2 = edt2.get() 
    data3 = edt3.get()
    try :
        sql = "INSERT INTO Student VALUES(" + data1 + ",'" + data2 + "','" + data3 + "')"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
    i+=1
    j+=2

def selectData() :
    i,j = 0,0
    strData1, strData2, strData3, strData4= [], [], [], []
    con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()
    cur.execute("SELECT * FROM Student")
    strData1.append("사용자 ID"); strData2.append("사용자 이름")
    strData3.append("전화번호"); strData4.append("이름 참조 목록 ")
    strData1.append("-----------"); strData2.append("-----------")
    strData3.append("-----------"); strData4.append("-----------")
    while(i<len(familyNames)) :
        strData4.append(familyNames[i]+firstNames[j]+firstNames[j+1])
        i+=1
        j+=2

    while (True) :
        row = cur.fetchone()
        if row== None :
            break;
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2])
        
    listData1.delete(0, listData1.size() - 1); listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1); listData4.delete(0, listData4.size() - 1)

    for item4 in strData4:
        listData4.insert(END, item4) 
    for item1, item2, item3 in zip(strData1, strData2, strData3):
        listData1.insert(END, item1); listData2.insert(END, item2)
        listData3.insert(END, item3)
    con.close()

def deleteData() :
    con, cur = None, None
    data= ""
    sql=""

    con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()
    data = edt4.get()
    try :
        sql = "DELETE FROM Student WHERE id=" + data
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()

def deleteAll() :
    con, cur = None, None
    data= ""
    sql=""

    con = sqlite3.connect("C:/projects/Pypractice/naverDB.db")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()
    data = edt4.get()
    try :
        sql = "DELETE FROM Student WHERE id<=" + data
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()  

#전역 변수   
familyNames = list("김이송박최정강조이장임한김고전홍박이김이나") #이름 20개
firstNames = list("태희영애혜교예진정현윤희수연가인수지미주은하채영성령아라인화진영초롱지은사랑주은석주")

## 메인 코드 부분 ## 
window = Tk()
window.geometry("950x450")
window.title("GUI 데이터 입력")

edtFrame = Frame(window);
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM,fill=BOTH, expand=1)

label1 = Label(edtFrame, text="id :", font=("돋음", 10)); label1.pack(side = LEFT, padx = 10, pady = 10)
edt1= Entry(edtFrame, width = 10); edt1.pack(side = LEFT, padx = 2, pady = 10)
label2 = Label(edtFrame, text="이름 :", font=("돋음", 10)); label2.pack(side = LEFT, padx = 10, pady = 10)
edt2= Entry(edtFrame, width = 10); edt2.pack(side = LEFT, padx = 2, pady = 10)
label3 = Label(edtFrame, text="전화번호 :", font=("돋음", 10)); label3.pack(side = LEFT, padx = 10, pady = 10)
edt3= Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 2, pady = 10)
label4 = Label(edtFrame, text="삭제할 id 값 :", font=("돋음", 10)); label4.pack(side = LEFT, padx = 10, pady = 10)
edt4= Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 2, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)

btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

btnSelect = Button(edtFrame, text = "삭제", command = deleteData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

btnSelect = Button(edtFrame, text = "모두 삭제", command = deleteAll)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'gray')
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

window.mainloop()