# 8.1

# is_even=lambda x: True if(x%2==0) else False
# print(is_even(8))

# is_leap=lambda x: True if(((x%4==0) and (x%100!=0)) or (x%400==0)) else False
# print(is_leap(2024))

# rev=lambda x:x[::-1]
# print(rev("Python"))

# maxi = lambda a,b:max(a,b)
# print(maxi(50,75))

# area_circle=lambda a:3.14*a*a
# print(area_circle(7))

# grade =lambda x:"A" if x>90 else "B" if x>75 else "C" if x>60 else "D" if x>40 else "F"
# print(grade(75))

# sort_insen = lambda word:word.sort(key=(str.lower))
# word=["Grape","Apple","banana","Zoo"]
# sort_insen(word)
# print(word)

funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)

print([f() for f in funcs])
