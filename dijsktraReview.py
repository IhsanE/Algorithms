#G=[[1000,45,200,97],[1000,1000,20,100],[1000,1000,1000,10],[1000,1000,1000,1000]]
G=[[1000,10,1000,30,100],[1000,1000,50,1000,1000],[1000,1000,1000,1000,10],[1000,1000,20,1000,60],[1000,1000,1000,1000,1000]]
def SP(G,start):
    seen=[True]+[False for i in range(len(G)-1)]
    q=G[start]
    path=[0,0,0,0]
    while(False in seen):
        v,d=1000,1000
        p=path
        for i in range(len(q)):
            if seen[i]==False:
                v = i if d>q[i] else v
                d = q[i] if d>q[i] else d
        seen[v]=True
        p.append(v)
        if min(G[v])+d < q[G[v].index(min(G[v]))]:
            q[G[v].index(min(G[v]))]= min(G[v])+d
            path[v]=p
    print (path)
    return q
print (SP(G,0))
