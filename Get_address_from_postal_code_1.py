#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import pprint


# In[28]:


#ユーザーからの入力を受け取る
#print('郵便番号を入力してください。（ハイフンなし半角）')
post_code =input('郵便番号を入力してください。（ハイフンなし半角）')
#print(post_code)
url = 'https://zipcloud.ibsnet.co.jp/api/search'

params = {'zipcode':post_code}

res = requests.get(url, params=params)

data = json.loads(res.text)
pprint.pprint(data['results'][0]['address1']+data['results'][0]['address2']
              +data['results'][0]['address3'])


# In[ ]:


#参考: https://office54.net/python/app/api-data-get
#HTTP 200 OK はリクエストが成功した場合に返すレスポンスコード。
#参考: https://developer.mozilla.org/ja/docs/Web/HTTP/Status/200

