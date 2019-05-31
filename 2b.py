def wpref(w,m,m1):
    global men,women,n
    for i in range(1,n+1):
        if women[w][i-1]==m:
            return True
        if women[w][i-1]==m1:
            return False

def matching():
    global men,women,n
    fcount=n
    fmen=[1 for i in range(n+1)]
    fwom=[1 for i in range(n+1)]
    pw=[(0,0) for i in range(n+1)]
    while fcount>0:
        for m in range(1,n+1):
            if fmen[m]==1:
                for i in range(1,n+1):
                    w=men[m][i-1]
                    if fwom[w]==1:
                        pw[w]=(m,w)
                        fcount-=1
                        fmen[m]=0
                        fwom[w]=0
                        break
                    else:
                        m1=pw[w][0]
                        if wpref(w,m,m1):
                            pw[w]=(m,w)
                            fmen[m]=0
                            fmen[m1]=1
                            break
    return pw

n=int(input("Enter number of men and women:"))
men=[0]
women=[0]
for i in range(1,n+1):
    temp=[]
    print("Enter preference list of man",i)
    for j in range(1,n+1):
        val=int(input())
        temp.append(val)
    men.append(temp)
for i in range(1,n+1):
    temp=[]
    print("Enter preference list of woman",i)
    for j in range(1,n+1):
        val=int(input())
        temp.append(val)
    women.append(temp)
print("Men's Preference List:",men[1:])
print("Women's Preference List:",women[1:])
pair=matching()
pair.sort(key=lambda x:x[0])
print("Stable Pairs(man,woman):",pair[1:])
print()
