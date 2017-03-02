import re
with open('../../input.in','r') as f:
	line_str=f.readline()
words=re.split(r'[\[\], "]+',line_str)
words.remove(words[0])
words.remove(words[-1])
row1=set('qwertyuiopQWERTYUIOP')
row2=set('asdfghjklASDFGHJKL')
row3=set('zxcvbnmZXCVBNM')
result_filter=filter(lambda x:set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3),words)
result_list=list(result_filter)
with open('../../output.out','w') as f:
	f.write(str(result_list))

class Solution(object):
	def findWords(self,words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		row1=set('qwertyuiopQWERTYUIOP')
		row2=set('asdfghjklASDFGHJKL')
		row3=set('zxcvbnmZXCVBNM')
		result_filter=filter(lambda x:set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3),words)
		result_list=list(result_filter)
		return result_list