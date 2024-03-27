import heapq
def goldenwire(lis):
    heapq.heapify(lis)
    tot=0
    while len(lis)>1:
        m1 = heapq.heappop(lis)
        m2 = heapq.heappop(lis)
        tot+=m1+m2
        heapq.heappush(lis,tot)
    return tot
        

    
    

l=[10,5,16,3,8,2,1]
print(goldenwire(l))
