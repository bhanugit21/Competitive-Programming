lis=[2,3,4,2,8]
k=2
new_lis=[]
kis=[]
for i in lis:
    if i==k:
        new_lis.append(i)
for i in range(len(new_lis)-1):
    kis.append(lis[new_lis[i]:new_lis[i+1]])
print(kis)
