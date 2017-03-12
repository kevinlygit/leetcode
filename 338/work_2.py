with open('../../input.in','r') as f:
	lineStr=f.readline()
num=int(lineStr)
resList=[bin(i).count('1') for i in range(num+1)]
with open('../../output.out','w') as f:
	f.write(str(resList))