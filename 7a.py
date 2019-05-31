n0=0
c=3
print("Value of c=",c)
print("n | f(n) | c*g(n)")
for n in range(10,31):
	fn=2*n*n+3*n+5
	gn=c*n
	if fn>=gn and n0==0:
		n0=n
	print(n," ",fn,"   ",gn)
print("n0=",n0)
