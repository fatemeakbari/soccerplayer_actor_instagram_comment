

f = open('n2.txt', 'r')

#recall actor
cnt = 0
pos = 0
neg = 0 
for line in f:
    line = line.rstrip()
    line = float(line)
    
    if cnt == 0:
        if line >= 0:
            pos = pos + 1
           
         
    if cnt == 1:
        if line >= 0:
            neg = neg + 1
            
    if cnt == 0:
        cnt = 1
    else:   
        cnt = 0      
        
print 'recall actor: '          
print   float(pos)/float(pos + neg)   #0.672040302267


#recall soccer
f = open('n2.txt', 'r')
cnt = 0
pos = 0
neg = 0 
for line in f:
    line = line.rstrip()
    line = float(line)
    
    if cnt == 0:
        if line <= 0:
            neg = neg + 1
           
         
    if cnt == 1:
        if line <= 0:
            pos = pos + 1
    if cnt == 0:
        cnt = 1
    else:   
        cnt = 0      
      
print 'recall soccer: '          
print  float(pos)/float(pos + neg)   #0.714915040906


#precit actor
f = open('n2.txt', 'r')
cnt = 0
pos = 0
neg = 0 
for line in f:
    line = line.rstrip()
    line = float(line)
    
    if cnt == 0:
        if line >= 0:
            pos = pos + 1
        else:
            neg = neg + 1
    if cnt == 0:
        cnt = 1
    else:   
        cnt = 0      
      
print 'preci actor: '          
print  float(pos)/float(pos + neg)   #0.7465



#precit soccer
f = open('n2.txt', 'r')
cnt = 0
pos = 0
neg = 0 
for line in f:
    line = line.rstrip()
    line = float(line)
    
    if cnt == 1:
        if line <= 0:
            pos = pos + 1
        else:
            neg = neg + 1
    if cnt == 0:
        cnt = 1
    else:   
        cnt = 0      
      
print 'preci soccer: '          
print  float(pos)/float(pos + neg)   #0.635702294348


