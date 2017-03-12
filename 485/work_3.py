import re
with open('../../input.in','r') as f:
	lineStr=f.readline()
lineList=re.split(r'[\[\],]+',lineStr)
lineList.remove(lineList[0])
lineList.remove(lineList[-1])
for i in range(len(lineList)):
	lineList[i]=int(lineList[i])
nums=lineList
resInt=max(list(map(len,''.join(list(map(str,nums))).split('0'))))
with open('../../output.out','w') as f:
	f.write(str(resInt))