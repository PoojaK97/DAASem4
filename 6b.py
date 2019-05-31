def merge(b,c,a):
	i=0 ; j=0 ; k=0
	global inv
	while i<len(b) and j<len(c):
		if b[i]<c[j]:
			a[k]=b[i]
			i+=1
		else:
			a[k]=c[j]
			j+=1
			inv+=len(b)-i
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
arr=[]
print("Enter list elements")
for i in range(n):
	val=int(input())
	arr.append(val)
print("List:",arr)
inv=0
msort(arr)
print("Sorted list:",arr)
print("Inversions=",inv)
