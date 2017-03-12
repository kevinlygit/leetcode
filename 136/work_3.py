import re
with open('../../input.in','r') as f:
	lineStr=f.readline()
lineList=re.split(r'[\[\],]+',lineStr)
lineList.remove(lineList[0])
lineList.remove(lineList[-1])
for i in range(len(lineList)):
	lineList[i]=int(lineList[i])
nums=lineList
dic={}
for num in nums:
	dic[num]=dic.get(num,0)+1
for key,val in dic.items():
	if val==1:
		resInt=key
with open('../../output.out','w') as f:
	f.write(str(resInt))