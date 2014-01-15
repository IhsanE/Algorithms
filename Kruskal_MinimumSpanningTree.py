import heapq
def Kruskal_MST(g):
    edgeList=[]
    vertexList=[[i] for i in range(len(g))]
    retList=[]
    for nOne in range(len(g)):
        for nTwo in range(len(g[nOne])):
            if (g[nOne][nTwo] != 0 and g[nOne][nTwo] != 100):
                heapq.heappush(edgeList,(g[nOne][nTwo],nOne,nTwo))
    for i in range(len(edgeList)):
        heapq.heapify(edgeList)
        edge=heapq.heappop(edgeList)
        nOne,nTwo=edge[1],edge[2]
        for sets in vertexList:
            if (nOne in sets):
                setOne=sets
            if (nTwo in sets):
                setTwo=sets
        if (setOne != setTwo):
            retList.append(edge)
            del(vertexList[vertexList.index(setOne)])
            del(vertexList[vertexList.index(setTwo)])
            vertexList.append(setOne+setTwo)
    return retList
g=[[0,7,100,5,100,100,100],[7,0,8,9,7,100,100],[100,8,0,100,5,100,100],[5,9,100,0,15,6,100],[100,7,5,15,0,8,9],[100,100,100,6,8,0,11],[100,100,100,100,9,11,0]]
print (Kruskal_MST(g))


    
