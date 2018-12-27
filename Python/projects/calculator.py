def calculate(x,y,ch) :
    """calculate(x,y,ch)->takes 2 integer x and y and perform their operation with ch operator which can be any of +,-,*      ,/,//,%,**"""
    if ch == '+' :
        return x + y
    elif ch == '-' :
        return x - y
    elif ch == '*' :
        return x * y
    elif ch == '/' :
        return x / y
    elif ch == '%' :
        return x % y
    else :
        return 'invalid character'
n=int(input("enter a number"))
s=int(input("enter another number"))
a=input("enter action to perform")
c = calculate(n,s,a)
print(c)
