inFp = None 
inList, inStr = [], ""

inFp = open("C:/projects/Pypractice/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    	print(inStr, end="")

inFp.close()