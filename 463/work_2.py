import re
import operator
with open('../../input.in','r') as f:
	linesList=f.readlines()
grid=[]
for lineStr in linesList:
	lineList=re.split(r'[\[\],\n]+',lineStr)
	lineList.remove(lineList[0])
	lineList.remove(lineList[-1])
	for i in range(len(lineList)):
		lineList[i]=int(lineList[i])
	grid.append(lineList)
a=(([sum(list(map(operator.ne,[0]+row,row+[0]))) for row in grid+list(map(list,zip(*grid)))]))
print(a)
resultInt=sum(sum(list(map(operator.ne,[0]+row,row+[0]))) for row in grid+list(map(list,zip(*grid))))
with open('../../output.out','w') as f:
	f.write(str(resultInt))