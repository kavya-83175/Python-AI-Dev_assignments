def rotate(arr,p,dum):
    k=0;
    for i in range(p,len(arr)):
        dum[k]=arr[i]
        k+=1
    for i in range(0,p):
        dum[k]=arr[i]
        k+=1
        

arr=list(map(int,input().split()))
k=int(input())
p=k%len(arr)
print(p)
dum=[0]*len(arr)
rotate(arr,p,dum)
print(dum)