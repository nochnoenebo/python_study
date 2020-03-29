def number(n):

    if n>21:
        result=(n-21)**2
    else:
        result=(21-n)
    return result
result=number(21)

print("результат:",result)