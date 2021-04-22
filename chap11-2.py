# 초기화------------------
inFp = None # 입력 파일
inList = []  # 읽어온 문자열 리스트로 저장

inFp = open("C:/projects/Pypractice/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
print(inList) # '\n'까지 읽음

inFp.close()

