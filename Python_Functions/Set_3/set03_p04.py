

p="I am global"
def check():
    p="I am enclosure"
    def check2():
        print(p);
        p="I am local"
    check2

print(p)
q=check()

