from sys import *
fi=open('Input.txt')
info=fi.readline().split()
nV,nE=info[0],info[-1]
aList=[]
for i in xrange(int(nV)+1):
  aList.append([maxint for x in xrange(int(nV)+1)])
for i in xrange(int(nE)):
  x=fi.readline().split()
  aList[int(x[0])][int(x[1])]=int(x[2])
	
def DSP(G,start,end):
  dist=G[start]
  seen=[]
  for i in xrange(len(G)):
    seen.append(False)
    seen[0]=True
  for i in xrange(len(G)-1):
    id=dist.index(min([dist[x] for x in xrange(len(dist)) if seen[x]==False]))
	
        	
    
DSP(aList,1,3)
