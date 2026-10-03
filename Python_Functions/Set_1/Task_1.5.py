def check(arr1,arr2):
    arr3=[]
    i,j=0,0
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<arr2[j]):
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        arr3.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        arr3.append(arr2[j])
        j+=1
    return arr3


arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(check(arr1,arr2))
