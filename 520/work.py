with open('../../input.in','r') as f:
	lineStr=f.readline()
word=lineStr
resBool=word.isupper() or word.islower() or word.istitle()
with open('../../output.out','w') as f:
	f.write(str(resBool))