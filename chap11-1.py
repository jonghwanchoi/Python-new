# 초기화------------------
inFp = None # 입력 파일
inStr = ""  # 읽어온 문자열

inFp = open("C:/projects/Pypractice/data1.txt", "r", encoding="utf-8")

# inStr = inFp.readline()
# print(inStr, end = "")

# inStr = inFp.readline()
# print(inStr, end = "")

while True :
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end = "")

inFp.close()

inFp.close()

