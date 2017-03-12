import re
with open('../../input.in','r') as f:
	lines_list=f.readlines()
findNums=re.split(r'[\[\],\n]+',lines_list[0])
findNums.remove(findNums[0])
findNums.remove(findNums[-1])
nums=re.split(r'[\[\],\n]+',lines_list[1])
nums.remove(nums[0])
nums.remove(nums[-1])
for i in range(len(findNums)):
	findNums[i]=int(findNums[i])
for i in range(len(nums)):
	nums[i]=int(nums[i])
stackList=[]
pointDictionary={}
for x in nums:
	if len(stackList)==0:
		stackList.append(x)
	elif x<stackList[-1]:
		stackList.append(x)
	else:
		while stackList and stackList[-1]<x:
			pointDictionary[stackList.pop()]=x
		stackList.append(x)
resultList=[]
for x in findNums:
	if x in pointDictionary:
		resultList.append(pointDictionary[x])
	else:
		resultList.append(-1)
with open('../../output.out','w') as f:
	f.write(str(resultList))