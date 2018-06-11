# - *- coding: utf- 8 - *-
from __future__ import unicode_literals
from hazm import *
from collections import Counter
import numpy as np


#tarin data##########################################################################################
soccerFile = 'soccer3Norm.txt'
soccerWords = open(soccerFile, 'r',encoding="utf-8").read().split()
filteredwords = [t for t in soccerWords]


numAllWord_soc = len(filteredwords)
soccerCounter = Counter(filteredwords)

soccerDic = dict(soccerCounter)



actorFile = 'actor3Norm.txt'
actorWords = open(actorFile, 'r',encoding="utf-8").read().split()
filteredwords = [t for t in actorWords]
numAllWord_act = len(filteredwords)

actorCounter = Counter(filteredwords)

actorDic = dict(actorCounter)



#test data####################################################################################
actor = open('actorTest.txt','r',encoding="utf-8")
soccer = open('soccerTest.txt','r')
act_cnt=0
soc_cnt=0
for line in actor:
    act_cnt +=1
    
for line in soccer:
    soc_cnt +=1  
     


act_label = np.full((act_cnt), 1)
soc_label = np.full((soc_cnt), -1)



############################################################################################################################
actor = open('actorTest.txt','r',encoding="utf-8")
soccer = open('soccerTest.txt','r')
 
normalizer = Normalizer()
lemmatizer = Lemmatizer()
tagger = POSTagger(model='resources-0.5/postagger.model')   
    
test_label_act = np.full((act_cnt),0) 
test_label_soc = np.full((soc_cnt),0) 
index = 0

def get_recall_precision(filename, one):
    index=0
    for line in filename:
        
        flag = False
        newLine =''
        line = normalizer.normalize(line)
        tokenList = word_tokenize(line)


        for token in tokenList:
            
            if (token[-2:] == 'ها'): 
                token = token[:-2]
            if (token[-3:] == 'های'):    
                token = token[:-3]
                
            verb = tagger.tag(word_tokenize(token))
            if(verb[0][1] == 'V'):
                token = lemmatizer.lemmatize(token)
                if(token.find('#') != -1):
                    token = token.split("#",1)[1]
             
             
            if(flag):
                newLine = newLine+' '+token
            else:
                newLine = token
            flag = True
            
             
        final_list = newLine.split()
        final_soc = 1
        final_act = 1
        for word in final_list:
            
            if word in soccerDic:    
                soc_rate = (soccerDic[word]+1)/float(numAllWord_soc)
            else:
                soc_rate = 1/float(numAllWord_soc + len(soccerCounter))        
            final_soc  *= soc_rate   
            
            if word in actorDic:    
                act_rate = (actorDic[word]+1)/float(numAllWord_act)
            else:
                act_rate = 1/float(numAllWord_act + len(actorCounter))        
            final_act  *= act_rate
                
            
        final_soc = final_soc *( float(numAllWord_soc)/(numAllWord_soc+numAllWord_act))
        final_act = final_act *( float(numAllWord_act)/(numAllWord_soc+numAllWord_act))
        print(final_soc)
        
        if(one):
            if(final_act >= final_soc):
                test_label_act[index] = 1
            else:
                test_label_act[index] = -1
            index +=1
        if(one == False):
            if(final_act <= final_soc):
                test_label_soc[index] = -1
            else:
                test_label_soc[index] = 1
            index +=1
        

    if(one):
        return test_label_act
    else:
        return test_label_soc




test_label_act = get_recall_precision(actor, True)
test_label_soc = get_recall_precision(soccer, False)



corr = 0
loss = 0
for i in range(0,len(test_label_act)):
    if(test_label_act[i] == 1):
        corr += 1
        
for i in range(0,len(test_label_soc)):
    if(test_label_soc[i] == 1):
        loss += 1 
         
precision = corr/float(act_cnt)
recall = corr/float(corr+loss)
print('precision actor: ',precision)
print('recall actor: ', recall)
        



corr = 0
loss = 0
for i in range(0,len(test_label_soc)):
    if(test_label_soc[i] == -1):
        corr += 1
        
for i in range(0,len(test_label_act)):
    if(test_label_act[i] == -1):
        loss += 1 
         
precision = corr/float(soc_cnt)
recall = corr/float(corr+loss)
print('precision soccer: ',precision)
print('recall soccer: ', recall)



'''
precision actor:  0.8786206896551724
recall actor:  0.8754810335349092
precision soccer:  0.8736049107142857
recall soccer:  0.8767852142257071

'''
