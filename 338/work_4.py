with open('../../input.in','r') as f:
	lineStr=f.readline()
num=int(lineStr)
resList=[0]
for i in range(1,num+1):
	cntInt=resList[i-(1<<(len(bin(i))-2))]+1
	resList.append(cntInt)
with open('../../output.out','w') as f:
	f.write(str(resList))