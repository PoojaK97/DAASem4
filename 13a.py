import random, time
n=int(input("Enter number of elements in list:"))
arr=[random.randint(1,50) for i in range(n)]
start=time.time()
print("List:",arr)
for i in range(1,n):
	for j in range(n-i):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
end=time.time()
print("Sorted List:",arr)
print("Time Taken: ",end-start)
