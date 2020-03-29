count = int(input())
if count%10==1 and count!=111 and count!=11 and count!=911 and count%100!=11:
    print (count,"программист")
elif (count%10==2 or count%10==3 or count%10==4) and count%100!=11 and count%100!=14 and count%100!=12 and count%100!=13:
    print (count,"программиста")
else:
    print (count,"программистов")