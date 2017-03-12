with open('../../input.in','r') as f:
	lineStr=f.readline()
s=lineStr
sList=list(s)
sList.reverse()
resultStr=''.join(sList)
with open('../../output.out','w') as f:
	f.write(resultStr)