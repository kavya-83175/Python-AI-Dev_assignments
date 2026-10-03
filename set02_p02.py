# 2.2 Flexible Calculator


def check(a,b,ope):
    if(ope=='+'):
        return a+b
    elif(ope=='-'):
        return a-b
    elif(ope=='*'):
        return a*b
    elif(ope=='/'):
        if(b==0):
            return f"Not valid"
        else:
            return a/b


a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
ope=input("Enter ope(+,-,*,/) : ")
print(check(a,b,ope))