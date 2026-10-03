# 3.1 Scope Puzzle Pack


# x = 10
# def f():
#     print(x)  #No local variable assigned so error      
#     x = 20    # Need to use (global x) to use global variable
# f()



# x = 5
# def f(x):
#     x = 10
# f(x)
# print(x)  #Output is 5 as (x=10) is local in function


# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         print(x)
#     inner()
# outer()


# if True:
#     z = 99
# print(z)