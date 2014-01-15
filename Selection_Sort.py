def SS(a,ret):
    if (len(a)<2):
        return ret
    else:
        min=a[0]
        for i in a[1:]:
            if min>i:
                min=i
        ret.append(min)
        a[a.index(min)],a[0]=a[0],min
        return SS(ret,a[1:])
print (SS([5,4,3,2,1],[]))
