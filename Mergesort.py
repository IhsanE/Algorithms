def Mergesort(a):
    high=len(a)-1
    if (high>0):
        mid=int(round((high)/2))
        if (mid==0):
            return Merge((a[:high]),(a[high:]))
        else:
            return Merge(Mergesort(a[0:mid]),Mergesort(a[mid:]))
            
def Merge(a,b):
    ret=[]
    length=len(a)+len(b)
    ai,bi=0,0
    while(len(ret)<length):
        if (len(a)==0):
            return ret+b
        elif (len(b)==0):
            return ret+a
        elif(a[ai]<b[bi]):
            ret.append(a[ai])
            del(a[ai])
        elif(b[bi]<=a[ai]):
            ret.append(b[bi])
            del(b[bi])
    print (ret)
    return ret
        
a=[6,5,3,1,8,10,7,2,4,9]
print(Mergesort(a))
