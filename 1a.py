import time, random

def rec_binsearch(L, key, high, low):
    mid=int((high+low)/2)
    if L[mid]==key:
        return mid
    elif L[mid]>key:
        return rec_binsearch(L, key, mid-1, low)
    else:
        return rec_binsearch(L, key, high, mid+1)
    return None

print("Enter the number of elements in the list")
n=int(input())
k=[random.randint(0,200) for i in range(0,n)]
print(k)
k.sort()
print("After sorting\n",k)
key=int(input("Enter key to be searched: "))
low=0
high=len(k)-1

start=time.time()
match=rec_binsearch(k, key, high, low)
time.sleep(1)

end=time.time()
if match==None:
    print("Unsuccessful")
else:
    print("Successful: Key fount at "+str(match+1)+" position")
    print("Time Taken: " + str(end-start) + " seconds")


#O{log n)
