import re
with open('../../input.in','r') as f:
	line=f.readline()
str_list=re.split(r'[\[", \]]+',line)
str_list.remove(str_list[0])
str_list.remove(str_list[-1])
result=filter(re.compile(r'(?i)(([qwertyuiop]*)|([asdfghjkl]*)|([zxcvbnm]*))$').match,str_list)
with open('../../output.out','w') as f:
	f.write(str(list(result)))