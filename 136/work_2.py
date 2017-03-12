import re
import operator
from functools import reduce
with open('../../input.in','r') as f:
	lineStr=f.readline()
lineList=re.split(r'[\[\],]+',lineStr)
lineList.remove(lineList[0])
lineList.remove(lineList[-1])
for i in range(len(lineList)):
	lineList[i]=int(lineList[i])
nums=lineList
resInt=reduce(operator.xor,nums)
with open('../../output.out','w') as f:
	f.write(str(resInt))