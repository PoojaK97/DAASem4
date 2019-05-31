def ins_sort():
	for i in range(1,n):
		v=arr[i]
		j=i-1
		while j>=0 and arr[j]>v:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=v

import random, time
n=int(input("Enter number of elements in list:"))
arr=[random.randint(1,50) for i in range(n)]
print("List:",arr)
start=time.time()
ins_sort()
time.sleep(1)
end=time.time()
print("Sorted Array:",arr)
print("Time Taken = "+str(end-start)+" seconds")
