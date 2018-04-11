# - *- coding: utf- 8 - *-
import requests


file1 = open('soccerComments.txt','r',encoding="utf-8")
file2 = open('rewriteSoccerComments.txt','wb') 

st = 'ا'
firstChar = st.encode("utf-8", errors='ignore')
st = 'ي'
lastChar = st.encode("utf-8", errors='ignore')
#print(encoded2)


flag =False    

for ch in file1:
    encoding = ch.encode("utf-8", errors='ignore')
    print(encoding)
    for i in range(0,len(encoding)):
        part = encoding[i:i+2]
        for j in range(0,len(part)):
            if( part[j] == 32):
                print(part[j])
                file2.write(b' ')
        if((encoding[i:i+2] <= lastChar and encoding[i:i+2] >= firstChar) or encoding[i:i+2] == b'\xda\x86' or
                                                            encoding[i:i+2] == b'\xd9\xbe' or
                                                            encoding[i:i+2] == b'\xda\xaf' or
                                                            encoding[i:i+2] == b'\xda\xa9' or
                                                            encoding[i:i+2] == b'\xda\x98' or
                                                            encoding[i:i+2] == b'\xdb\x8c' or
                                                            encoding[i:i+2] == b'\xd8\xa6' or
                                                            encoding[i:i+2] == b'\xd8\xa2'
        ):
            file2.write(encoding[i:i+2])
            flag = True
    if (flag):
        file2.write(b'\n')
    flag = False
    print('\n')
    

file2.close()



