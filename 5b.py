def merge(b,c,a):
	i=0 ; j=0 ; k=0
	while i<len(b) and j<len(c):
		if b[i]<c[j]:
			a[k]=b[i]
			i+=1
		else:
			a[k]=c[j]
			j+=1
		k+=1
	while i<len(b):
		a[k]=b[i]
		i+=1
		k+=1
	while j<len(c):
		a[k]=c[j]
		j+=1
		k+=1

def msort(a):
	if len(a)>1:
		mid=len(a)//2
		llist=a[:mid]
		rlist=a[mid:]
		msort(llist)
		msort(rlist)
		merge(llist,rlist,a)

import random,time
n=int(input("Enter number of elements in list:"))
arr=[random.randint(0,50) for i in range(n)]
print("List:",arr)
start=time.time()
msort(arr)
end=time.time()
print("Sorted list:",arr)
print("Total time taken for execution=",end-start)
