def composition(c,d):
    if c==d:
        result=(c+d)
    else:
        result=(c*d)
    return result


result=composition(12,23)

print("результат:",int(result))
print (1.2345e-3)





a=int(input("введите число a:"))
b=int(input("введите число б:"))
if a==b:
    result1=(a+b)
    print("a+b=",int(result1))
else:
    result1=(a*b)
    print("a*b=", int(result1))