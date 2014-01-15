from heapq import *
#G=[[1000,10,3,1000,1000],[1000,1000,1,2,1000],[1000,4,1000,8,2],[1000,1000,1000,1000,7],[1000,1000,1000,9,1000]]
G=[[1000,10,1000,30,100],[1000,1000,50,1000,1000],[1000,1000,1000,1000,10],[1000,1000,20,1000,60],[1000,1000,1000,1000,1000]]
def djikstra(G,s):
    dist=G[s][:]
    Q=[(G[s][i],i) for i in range(len(G))]
    path=[(s,i)for i in range(len(G))]
    path[s]=s,
    heapify(Q)
    while(Q):
        d,v=heappop(Q)
        for vertex,distance in enumerate(G[v]):
            if dist[vertex] > d+distance:
                dist[vertex] = d+distance
                path[vertex] = path[v]+(vertex,)
                heappush(Q,(d+distance,vertex))
    return dist,path

print (djikstra(G,0))

#a=[7**i%(2**16-1)for i in xrange(100,200)]
#print a
#heapify(a)
#print a
#while a:
#    print heappop(a)
