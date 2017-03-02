with open('../../input.in','r') as f:
	lines=f.readlines()
xylist=lines[0].split(' ')
x=int(xylist[0])
y=int(xylist[1])
binary=bin(x^y)
print(binary)
print(type(binary))
result=bin(x^y).count('1')
with open('../../output.out','w') as f:
	f.write(str(result))