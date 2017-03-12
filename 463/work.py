import re
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

def sum_adjacent(i,j):
	adjacent=[[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
	count=0
	for x,y in adjacent:
		if x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y]==0:
			count+=1
	return count

result=0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j]==1:
			result+=sum_adjacent(i,j)
with open('../../output.out','w') as f:
	f.write(str(result))