#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import requests

url = 'https://www.instagram.com/p/BcSRzebgJoq/?taken-by=mohamadreza9999'
req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
media_id = req.json()['media_id']


# stop conditions, the script will end when first of them will be true
until_date = '2017-03-31'
count = 1500

API = InstagramAPI("fa_i_u", "1234Fa56")
API.login()
#API.getUsernameInfo('mahnaz_afshar')
has_more_comments = True
max_id = ''
comments = []
cnt = 0
file1 = open('soccerComments.txt','a')
while has_more_comments:
    cnt +=1
    
    _ = API.getMediaComments(media_id, max_id=max_id)
    # comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        comments.append(c)
        text = c['text']
	
        txt = text.encode('utf-8')
        
	file1.write(txt+'\n')
        
    
    has_more_comments = API.LastJson.get('has_more_comments', True)
    
    
    # evaluate stop conditions
    if count and len(comments) >= count:
        comments = comments[:count]
        # stop loop
        has_more_comments = False
        print ("stopped by count")
    if until_date:
        
        older_comment = comments[-1]
        dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
        # only check all records if the last is older than stop condition
        
        if dt.isoformat() <= until_date:
            print('secces2')
            # keep comments after until_date
            comments = [
                c
                for c in comments
                if datetime.utcfromtimestamp(c.get('created_at_utc', 0)) > until_date
            ]
            # stop loop
            has_more_comments = False
            print ("stopped by until_date")
    # next page
    print('has_more_comments2   ',has_more_comments)
    if has_more_comments:
        print('secces3')
        max_id = API.LastJson.get('next_max_id', '')
        #
        #print('id  ', max_id)
        time.sleep(2)

file1.close()


