from collections import deque
def bfs (s, adj):
  level = {s:0}
  parent={s:None}
  i = 1
  frontier = [s]
  while frontier:
    next=[]
    for u in frontier:
      for v in adj[u]:
        if v not in level:
          level[v]=i
          parent[v] = u
          next.append(v)
    frontier = next
    i+=1
  return parent


fi=open('GRAPH_BFS.txt')
T=int(fi.readline())
adj = {}
for t in range(T):
  vertex = fi.readline().strip()
  line = fi.readline().strip()
  adj[vertex] = [x for x in line]
p = bfs("A", adj)
print p
familyTree = zip([x for x in p],[p[x] for x in p])
print familyTree
answer=[]
search = "V"
for i in familyTree:
  print i[1]
  if i[1] == search:
    search = i[0]
    answer.append(search)
    
      


