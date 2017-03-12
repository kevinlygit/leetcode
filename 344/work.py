with open('../../input.in','r') as f:
	lineStr=f.readline()
s=lineStr
resultStr=s[::-1]
with open('../../output.out','w') as f:
	f.write(resultStr)