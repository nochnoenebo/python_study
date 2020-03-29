a, b, c = int(input()), int(input()), int(input())
if a>b and a>c:
    x=a
elif b>a and b>c:
    x=b
elif a==b and a>c:
    x=a
elif a==c and a>b:
    x=a
elif b==c and b<a:
    x=a
else:
    x=c

if a<b and a<c:
    y=a
elif b<a and b<c:
    y=b
elif a==b and a<c:
    y=b
elif a==c and a<b:
    y=a
elif c==b and c<b:
    y=c
else:
    y=c

print (x, y, ((a+b+c)-(x+y)), sep="\n")