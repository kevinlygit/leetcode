with open('../../input.in','r') as f:
	lineStr=f.readline()
s=lineStr
resultStr=''.join(list(reversed(s)))
with open('../../output.out','w') as f:
	f.write(resultStr)