def mystery(a, b=[], *c, **d):
    b.append(a)
    return a, b, c, d

print(mystery(1))
print(mystery(2, [9]))
print(mystery(3))
print(mystery(4, [7], 8, 9, x=10))
