from heapq import *
G=[[0,1,4,100,100],[100,0,2,5,12],[100,100,0,2,100],[100,100,100,0,3],[100,100,100,100,0]]
H=[7,6,2,1,0]
def A(G,H,start,end):
    #qNode=(F-score,Vertex,G-score) // H-score referenced from table
    q=[(H[start]+0,str(start),0)]
    while(q):
        heapify(q)
        node=heappop(q)
        f,v,g=node[0],node[1],node[2]
        if int(v[-1])==end:
            return v,f
        else:
            for edges in xrange(len(G)):
                if G[int(v[-1])][edges] != 100 and  G[int(v[-1])][edges] != 0:
                    heappush(q,(H[edges]+G[int(v[-1])][edges]+g,v+str(edges),G[int(v[-1])][edges]+g))
    return None
print A(G,H,0,4)
