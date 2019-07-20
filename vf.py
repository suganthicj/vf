X1,Y1=map(int,input().split())
Z1=[]
for i in range(X1+1,Y1+1):
    if(i%2!=0):
     Z1.append(i)
print(*Z1,sep=" ")
