import re
with open('../../input.in','r') as f:
	line_str=f.readline()
words=re.split(r'[\[\], "]+',line_str)
words.remove(words[0])
words.remove(words[-1])
ans=[word for word in words for row in ('qwertyuiop','asdfghjkl','zxcvbnm') if set(word.lower())<=set(row)]
with open('../../output.out','w') as f:
	f.write(str(ans))