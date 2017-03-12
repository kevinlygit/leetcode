def reverseString(s):
	nLen=len(s)
	if nLen<=1:
		return s
	return reverseString(s[nLen//2:])+reverseString(s[:nLen//2])
with open('../../input.in','r') as f:
	lineStr=f.readline()
s=lineStr
resultStr=reverseString(s)
with open('../../output.out','w') as f:
	f.write(resultStr)