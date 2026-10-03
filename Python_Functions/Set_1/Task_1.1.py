# Task 1.1 : Cricket Analyser

# Output:
# Total runs      : 68
# Highest over    : 20
# Lowest over     : 0
# Average per over: 8.5
# Maiden overs    : 1
# Bytes used      : 32


def max_runs_over(arr):
    ans=0
    for i in arr:
        ans=max(ans,i)
    return ans

def min_runs_over(arr):
    ans=arr[0]
    for i in arr:
        ans=min(ans,i)
    return ans

def tot_runs(arr):
    ans=0
    for i in arr:
        ans+=i
    return ans

def madin(arr):
    return arr.count(0)

def avg_per_over(arr):
    return sum(arr)/len(arr)

def bytes_used(arr):
    return 4*len(arr)

arr=list(map(int,input().split()))
print("Highest over : ",max_runs_over(arr))
print("Lowest over : ",min_runs_over(arr))
print("Total runs : ",tot_runs(arr))
print("Average per over : ",avg_per_over(arr))
print("Maiden overs : ",madin(arr))
print("Bytes : ",bytes_used(arr))
