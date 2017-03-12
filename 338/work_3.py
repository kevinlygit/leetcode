with open('../../input.in','r') as f:
	lineStr=f.readline()
num=int(lineStr)
resList=[]
for i in range(num+1):
	binStr=bin(i)[2:]
	oneStr=binStr.replace('0','')
	cntInt=len(oneStr)
	resList.append(cntInt)
with open('../../output.out','w') as f:
	f.write(str(resList))