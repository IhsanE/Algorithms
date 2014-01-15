import math 
def Heapify(A): 
    retArray=[] 
    while(A): 
        newNode=A.pop() 
        retArray.append(newNode) 
        curNode=int(len(retArray)-1) 
        compareNode=int(math.ceil((len(retArray)-1)/2)-1) 
        if (retArray[compareNode]<newNode): 
            while(compareNode>-1 and curNode>-1): 
                if(retArray[compareNode]>newNode): 
                    break
                else: 
                    retArray[curNode]=retArray[compareNode] 
                    retArray[compareNode]=newNode 
                    curNode,compareNode=compareNode,math.ceil(curNode/2)-1
    return retArray

def Heapsort(A,retArray):
    if (A):
        retArray.append(A[0])
        A[0]=A[-1]
        del(A[-1])
        parent,child1,child2=0,1,2
        print (A)
        while(child1 < len(A) or child2 < len(A)):
            if (A[parent]<A[child1] or A[parent]<A[child2]):
                if (child1<len(A) and child2<len(A)):
                    maxx=max(A[child1],A[child2])
                    i=A.index(max(A[child1],A[child2]))
                elif (child1<len(A) and child2 >=len(A)):
                    maxx=A[child1]
                    i=child1
                else:
                    maxx=A[child2]
                    i=child2
            else:
                break
            A[i],A[parent]=A[parent],maxx
            parent=i
            child1,child2=(2*(parent+1)-1),(2*(parent+1))
        return Heapsort(A,retArray)
    else:
        return retArray[::-1]

a=[41,67,34,0,69,24,78,58,62,64,5,45,81,27,61] 
a=a[::-1] 
    
print (Heapsort([11,10,9,4,3,5,7],[]))
print (Heapsort(Heapify(a),[]))
print(Heapsort(Heapify([10,9,8,7,6,5,4,3,2,1]),[]))
