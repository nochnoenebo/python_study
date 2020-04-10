gc=input()
j=0
f=0
for i in gc.lower():
    if i=='c' or i=='g':
        j+=1
    f+=1
print (j/f*100)