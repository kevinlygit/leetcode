with open('../../input.in','r') as f:
	line_str=f.readline()
n=int(line_str)
ans=[('Fizz'*(not i%3)+'Buzz'*(not i%5)) or str(i) for i in range(1,n+1)]
with open('../../output.out','w') as f:
	f.write(str(ans))