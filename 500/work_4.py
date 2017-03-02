import re
with open('../../input.in','r') as f:
	line_str=f.readline()
words=re.split(r'[\[\], "]+',line_str)
words.remove(words[0])
words.remove(words[-1])
a=set('qwertyuiop')
b=set('asdfghjkl')
c=set('zxcvbnm')
ans=[]
for word in words:
	t=set(word.lower())
	if a&t==t:
		ans.append(word)
	if b&t==t:
		ans.append(word)
	if c&t==t:
		ans.append(word)
with open('../../output.out','w') as f:
	f.write(str(ans))