with open('../../input.in','r') as f:
	line_str=f.readline()
n=int(line_str)
ans=[str(i)*(i%3!=0 and i%5!=0)+'Fizz'*(i%3==0)+'Buzz'*(i%5==0) for i in range(1,n+1)]
with open('../../output.out','w') as f:
	f.write(str(ans))