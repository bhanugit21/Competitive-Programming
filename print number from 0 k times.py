t=int(input())
n=int(input())
i=0
while t>0:
    print(i)
    i=(i+1)%n
    t-=1
