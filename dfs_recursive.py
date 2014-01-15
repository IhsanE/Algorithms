Graph = [0,[2,7,8],[1,3,6],[2,4,5],[3],[3],[2],[1],[1,9,12],[8,10,11],[9],[9],[8]]
def dfs(G,s,seen):
    for edge in G[s]:
         if edge not in seen:
            seen.append(edge)
            dfs(G,edge,seen)
    return seen
seen=[1]
print dfs(Graph,1,seen)
                
