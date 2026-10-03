
x=100
def check(a):
    global x
    if (x>=a):
        x-=a
    else:
        print("Not enough seats")

check(5)
# print(x)
check(63)
print(x)
