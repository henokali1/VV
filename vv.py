import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vv.settings')

import django
django.setup()
from django.core.wsgi import get_wsgi_application
from products.models import *

import pickle

import urllib.parse
import ast
import requests
import time
import json
import datetime

application = get_wsgi_application()


def req(pageNum):
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Authorization': 'Token 1ef030d1b8eeade369342e2a32065564dfd268b7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': '_gid=GA1.2.827542006.1584819998; _fbp=fb.1.1584819998864.607313022; _etison_sessions_dcs_v2=88dd471cdaf064340035371c96e85a73; __stripe_mid=3f8b4907-9f9b-483f-a1fb-3c25e117346e; __stripe_sid=cd4cf61c-f35f-41c3-b0f4-f5ad635ca8de; messages="bd7e4aef0b649bef35a2f1e00b9901e80f9079c3$[[\"__json_message\"\0540\05420\054\"Confirmation e-mail sent to okarshop@gmail.com.\"]\054[\"__json_message\"\0540\05425\054\"You have confirmed okarshop@gmail.com.\"]]"; token=1ef030d1b8eeade369342e2a32065564dfd268b7; _ga=GA1.1.20035854.1584819998; _ga_804328453=GS1.1.1584819994.1.1.1584820730.0; csrftoken=U1IHLBAFOzdFTectJmS3nW2tvClXTKDDVFl5bLiDTt6XbyxEJEUHIfTq6bAWoc6T; sessionid=scgpvpkgq3iwmh7meuro3zx1lbcawc8o',
        'Host': 'app.tryviralvault.com',
        'Referer': 'https://app.tryviralvault.com/trending',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }

    url = 'https://app.tryviralvault.com/api/v1/product/product/?page={}'.format(pageNum)
    t = time.time()
    response = requests.get(url, headers=headers)
    tt = round(time.time() - t, 1)
    r = json.loads(response.text)
    print('--------------------------------------------------')
    print('Request compleated in {} secs'.format(tt))
    print('--------------------------------------------------')
    
    new_data = RawData()
    new_data.data = r
    new_data.save()
        

for i in range(1000):
    print('page ', i+1)
    r = req(i+1)

