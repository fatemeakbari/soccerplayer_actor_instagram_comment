# - *- coding: utf- 8 - *-
f1 = open('rewriteActor.txt','r')
f2 = open('rewriteSoccer.txt','r')
f3 = open('voubal.txt','w')

flag = True
for i in range(0,10000):
    cnt1 = 0;
    cnt2 = 0;
    
    for line in f1:
        if(cnt1 == 0):
            f3.write('1 | '+line)
            
            cnt1 +=1
        if( cnt1 == 1):
            break
       
    for line in f2:
        if(cnt2 == 0):
            f3.write('-1 | ' +line)
            cnt2 +=1
        if( cnt2 == 1):
            break
            
            
