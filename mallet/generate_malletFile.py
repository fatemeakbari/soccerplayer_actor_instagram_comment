
# - *- coding: utf- 8 - *-
from __future__ import unicode_literals
from hazm import *


normalizer = Normalizer()
lemmatizer = Lemmatizer()

#tagger = POSTagger(model='resources-0.5/postagger.model')

input_file = open('train.txt', 'r')
output = open('input.txt','w')
cnt = 0
count = 0
for line in input_file:
   
    write_line=''         
     #line = unicode(line, "utf-8")
    #print(type(line))
    line = normalizer.normalize(line)
    token_list2 = [] 
    tokenList = word_tokenize(line)
    for token in tokenList:
          
        flag = True
        if (token[-2:] == 'ها'): 
            token = token[:-2]
        if (token[-3:] == 'های'):
            token =token[:-3]
        token_list2.append(token)
        
    f1 = f2 =f3=f4=f5=f6=f7=f8=f9=f10=f11=f12=f13=f14=f15=f16=0
    
    if(cnt == 0):
        if('کانال' in token_list2):
            f2 =+ 1
        if('پایتخت' in token_list2):
            f3 =+ 1    
        if('پیج' in token_list2):
            f4 =+ 1
        if('لایک' in token_list2):
            f5 =+ 1        
        if('فالو' in token_list2):
            f6 =+ 1        
        if('تلگرام' in token_list2):
            f7 =+ 1               
        if('خانم' in token_list2):
            f8 =+ 1        
        if('سریال' in token_list2):
            f9 =+ 1        
        if('رایگان' in token_list2):
            f10 =+ 1        
        if('دایرکت' in token_list2):
            f11 =+ 1        
        if('عالی' in token_list2):
            f12 =+ 1        
        if('سلام' in token_list2):
            f13 =+ 1        
        if('سال' in token_list2):
            f14 =+ 1        
        if('فیلم' in token_list2):
            f15 =+ 1 
        
        
    if(cnt == 1):    
        
        if('کاپیتان' in token_list2):
            f2 =+ 1    
        if('گل' in token_list2):
            f3 =+ 1
        if('پرسپولیس' in token_list2):
            f4 =+ 1        
        if('برگرد' in token_list2):
            f5 =+ 1        
        if('بمون' in token_list2):
            f6 =+ 1        
        if('پسر' in token_list2):
            f7 =+ 1        
        if('تیم' in token_list2):
            f8 =+ 1        
        if('داداش' in token_list2):
            f9 =+ 1        
        if('عشقی' in token_list2):
            f10 =+ 1        
        if('قهرمان' in token_list2):
            f11 =+ 1        
        if('قهرمانی' in token_list2):
            f12 =+ 1        
        if('اقا' in token_list2):
            f13 =+ 1        
        if('بازیکن' in token_list2):
            f14 =+ 1        
        if('مهندس' in token_list2):
            f15 =+  1
            
    if(cnt == 0 and len(token_list2) >0):
        write_line = str(count) +' actor'+ ' f1=' + token_list2[0] +' f2=' + str(f2) +' f3=' +str(f3) +' f4=' + str(f4) +' f5='+str(f5)+  \
        ' f6=' +str(f6) +' f7=' + str(f7) +' f8=' +str(f8) +' f9=' + str(f9) +' f10=' +str(f10) +' f11=' + str(f11) +' f12=' +str(f12) +' f13=' + str(f13) +' f14=' +str(f14)+' f15=' +str(f15)
        
    if(cnt == 1 and len(token_list2) >0):
        write_line = str(count) +' soccer '+ ' f1=' + token_list2[0] +' f2=' + str(f2) +' f3=' +str(f3) +' f4=' + str(f4) +' f5='+str(f5)+  \
        ' f6=' +str(f6) +' f7=' + str(f7) +' f8=' +str(f8) +' f9=' + str(f9) +' f10=' +str(f10) +' f11=' + str(f11) +' f12=' +str(f12) +' f13=' + str(f13) +' f14=' +str(f14)+' f15=' +str(f15)
        
        
    output.write(write_line)
    output.write('\n') 
    if(cnt == 0):
        cnt = 1
    else:
        cnt = 0
    count = count +1        
        
output.close()           
