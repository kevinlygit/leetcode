import re
with open('../../input.in','r') as f:
	line_str=f.readline()
words=re.split(r'[\[\], "]+',line_str)
words.remove(words[0])
words.remove(words[-1])
row=['qwertyuiopQWERTYUIOP','asdfghjklASDFGHJKL','zxcvbnmZXCVBNM']
ans=[]
for word in words:
	which=None
	good=True
	for s in word:
		if which==None:
			for k,v in enumerate(row):
				if s in v:
					which=k
		else:
			if s not in row[which]:
				good=False
				break
	if good:
		ans.append(word)
with open('../../output.out','w') as f:
	f.write(str(ans))