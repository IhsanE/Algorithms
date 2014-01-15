Graph = [0,[8,7,2],[6,3,1],[5,4,2],[3],[3],[2],[1],[12,9,1],[11,10,8],[9],[9],[8]]

def dfs(G,s):
    frontier=[s]
    marked=[s]
    while frontier:
        v = frontier.pop()
        print v
        for edge in G[v]:
            if edge not in marked:
                marked.append(edge)
                frontier.append(edge)
    return marked

print dfs(Graph,1)
                
