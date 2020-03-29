import math
S = input()
if S =='треугольник':
    a=int(input())
    b=int(input())
    c=int(input())
    p=1/2*(a+b+c)
    print (math.sqrt(p*((p-a)*(p-b)*(p-c))))
elif S =='прямоугольник':
    a=int(input())
    b = int(input())
    print(a * b)
elif S =='круг':
    r=int(input())
    print((r**2)*3.14)
else:
    print ('не умею')





a = float(input())
b = float(input())
c = input()
if b==0.0 and (c=="div" or c=="/" or c=="mod"):
    print ('Деление на 0!')
elif c=='+':
    print(a + b)
elif c=='-':
    print(a - b)
elif c=='/':
    print(a / b)
elif c=='*':
    print(a * b)
elif c=='mod':
    print (a%b)
elif c=='pow':
    print (a**b)
elif c=='div':
    print (a//b)
else:
    print('не знаком с данной операцией')

a = int(input())
if -15<a<=12 or 14<a<17 or a>19:
    print('True')
else:
    print('False')