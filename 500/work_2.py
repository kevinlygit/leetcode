import re
with open('../../input.in','r') as f:
	line_str=f.readline()
words_list=re.split(r'[\[", \]]+',line_str)
words_list.remove(words_list[0])
words_list.remove(words_list[-1])
result_list=[word for row in [set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')] for word in words_list if set(word.lower())<=row]
with open('../../output.out','w') as f:
	f.write(str(result_list))