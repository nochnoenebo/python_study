
A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально')
elif A > H:
    print('Недосып')
else:
    print('Пересып')


year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('Високосный')
elif year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')

X = int(input())
H = int(input())
M = int(input())
B=H*60+M
print((X+B)//60)
print((X+B)%60)