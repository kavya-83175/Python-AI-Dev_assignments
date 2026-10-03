# 2.3 URL Query Builder 

def check(**filters):
    ans=""
    for key,value in filters.items():
        ans+=f"{key}={value}&"
    if (ans):
        ans=ans[:-1]
    return ans

print(check(city="Hyderabad",food="Biryani",rating=5))
