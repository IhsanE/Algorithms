def dfs(G,s):
  parent={s:None}
  frontier=[s]
  while (frontier):
    v=frontier.pop()
    for i in G[v]:
      if i not in parent:
        parent[i]=v
        frontier.append(i)
  return parent

#goal=int(raw_input())

# str = n c


def factor(n):
  factors=[1,n]
  for i in xrange(2,n/2+1):
    if n%i==0:
      factors.append(i)
  return factors
print factor(1)
G={}
G[1]=factor(1)
for i in xrange(5):
  
