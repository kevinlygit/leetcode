with open('../../input.in','r') as f:
	lineStr=f.readline()
n=int(lineStr)
resBool=(n%4!=0)
with open('../../output.out','w') as f:
	f.write(str(resBool))