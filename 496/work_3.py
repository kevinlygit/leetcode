import re
with open('../../input.in','r') as f:
	linesList=f.readlines()
findNums=re.split(r'[\[\],]+',linesList[0])
findNums.remove(findNums[0])
findNums.remove(findNums[-1])
for i in range(len(findNums)):
	findNums[i]=int(findNums[i])
nums=re.split(r'[\[\],]+',linesList[1])
nums.remove(nums[0])
nums.remove(nums[-1])
for i in range(len(nums)):
	nums[i]=int(nums[i])
stackList=[]
hDict={}
for x in nums:
	while stackList and stackList[-1]<x:
		hDict[stackList.pop()]=x
	stackList.append(x)
resultList=[hDict.get(x,-1) for x in findNums]
with open('../../output.out','w') as f:
	f.write(str(resultList))