def partition(l,r):
	global a
	i=l+1
	j=r
	pivot=a[l]
	while True:
		while i<=j and a[i]<=pivot:
			i+=1
		while i<=j and a[j]>=pivot:
			j-=1
		if i>j:
			break
		else:
			a[i],a[j]=a[j],a[i]
	a[l],a[j]=a[j],a[l]
	return j
def qsort(l,r):
	if l<r:
		mid=partition(l,r)
		qsort(l,mid-1)
		qsort(mid+1,r)

import random,time
n=int(input("Enter number of elements in list:"))
a=[random.randint(1,50) for i in range(n)]
print("List:",a)
start=time.time()
qsort(0,n-1)
end=time.time()
print("Sorted list:",a)
print("Execution time=",end-start)
