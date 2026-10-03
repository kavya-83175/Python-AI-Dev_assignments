

def second_max(arr,maxi):
    p=-1
    for i in arr:
        if (i!= maxi):
            p=max(p,i)
    return p
    

arr=list(map(int,input().split()))
maxi=max(arr)
if(second_max(arr,maxi)==-1):
    print("No Second largest")
else:
    print("Second largest : ",second_max(arr,maxi))
