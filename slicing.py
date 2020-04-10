# s = 'abcdefghijk'
# print (s[3:6])
# print (s[:6])
# print (s[3:])
# print (s[::-1])
# print (s[-3:])
# print (s[:-6])
# print (s[-1:-10:-2])
s = 'aaaabbсaa'
i=0
j=int(len(s))
count=0
for i in range(j):
     if s[i]==s[i+1]:
         count+=1
     print(i, count)

print (j+1)
print(i)