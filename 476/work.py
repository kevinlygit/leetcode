with open('../../input.in','r') as f:
	line=f.read()
num=int(line)
mask=(1<<(len(bin(num))-2))-1
result=mask^num
with open('../../output.out','w') as f:
	f.write(str(result))

class Solution(object):
	def findComplement(self,num):
		"""
		:type num: int
		:rtype: int
		"""
		return ((1<<(len(bin(num))-2))-1)^num