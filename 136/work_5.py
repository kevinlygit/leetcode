import re
from collections import Counter
with open('../../input.in','r') as f:
	lineStr=f.readline()
lineList=re.split(r'[\[\],]+',lineStr)
lineList.remove(lineList[0])
lineList.remove(lineList[-1])
for i in range(len(lineList)):
	lineList[i]=int(lineList[i])
nums=lineList
a=Counter(nums)
for k,v in a.items():
	if v<2:
		resInt=k
with open('../../output.out','w') as f:
	f.write(str(resInt))