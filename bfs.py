G={"A":["B","C","D"],"B":["A","E","F"],"C":["A","F"],"D":["A"],"E":["B"],"F":["B","C"]}
def bfs(G,v):
    node=0
    parent={v:None}
    q=[v]
    for v in q:
        for i in G[v]:
            if i not in parent.values():
                parent[i]=v
                q.append(i)
    return parent
print (bfs(G,"A"))

    
