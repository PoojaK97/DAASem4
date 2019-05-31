import random

n=int(input("Enter number of elements in list:"))
arr=[random.randint(0,200) for i in range(n)]
print("List:",arr)
for i in range(n):
	minn=i
	for j in range(i+1,n):
		if arr[j]<arr[minn]:
			minn=j
	arr[i],arr[minn]=arr[minn],arr[i]
print("Sorted list:",arr)
