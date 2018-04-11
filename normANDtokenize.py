
from __future__ import unicode_literals
from hazm import *

file1 = open('rewriteSoccerComments.txt','r')
file2 = open('soccerNorm.txt','w')

normalizer = Normalizer()
lemmatizer = Lemmatizer()

tagger = POSTagger(model='resources-0.5/postagger.model')



flag = True
for line in file1:
     line = normalizer.normalize(line)
     tokenList = word_tokenize(line)
     for token in tokenList:
          
          flag = True
          if (token[-2:] == 'ها'): 
               token = token[:-2]
          if (token[-3:] == 'های'):
               token =token[:-3]
          if( token == 'من' or token == 'تو' or token == 'او' or token == 'ما' or  token == 'شما' or token == 'ایشان' or token == 'که' or token == 'به' or 
               token == 'هر' or token == 'اگر' or token == 'یا' or token == 'بی' or token == 'یه' or token == 'تا' or token == 'هم' or token == 'در' or 
               token == 'را' or token == 'بر' or token == 'ای' or token == 'از' or token == 'با' or token == 'و'):
               
               flag = False
         
          verb = tagger.tag(word_tokenize(token))
          if(verb[0][1] == 'V'):
               token = lemmatizer.lemmatize(token)
               if(token.find('#') != -1):
                    token = token.split("#",1)[1]
          
          if(flag):     
               file2.write(token)
               file2.write('\n')

file2.close()
