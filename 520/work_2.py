with open('../../input.in','r') as f:
	lineStr=f.readline()
word=lineStr
resBool=word in [word.upper(),word.lower(),word.capitalize()]
with open('../../output.out','w') as f:
	f.write(str(resBool))