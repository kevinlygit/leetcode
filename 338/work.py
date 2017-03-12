with open('../../input.in','r') as f:
	lineStr=f.readline()
num=int(lineStr)
binList=[0]
while len(binList)<=num:
	binList+=[i+1 for i in binList]
resList=binList[:num+1]
with open('../../output.out','w') as f:
	f.write(str(resList))