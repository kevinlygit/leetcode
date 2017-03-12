import re
with open('../../input.in','r') as f:
	lineStr=f.readline()
lineList=re.split(r'[\[\],]+',lineStr)
lineList.remove(lineList[0])
lineList.remove(lineList[-1])
for i in range(len(lineList)):
	lineList[i]=int(lineList[i])
nums=lineList
resInt=0
cntInt=0
for num in nums:
	if num==1:
		cntInt+=1
		resInt=max(resInt,cntInt)
	else:
		cntInt=0
with open('../../output.out','w') as f:
	f.write(str(resInt))