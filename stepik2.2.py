q='qwe'
while q:
    a = int(input())
    if a<10:
        continue #пропуск числа
    if a>100:
        break
    else:
        print(a)