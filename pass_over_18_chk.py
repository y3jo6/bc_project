# coding: utf-8
#try upload

# In[1]:

import requests


# In[6]:

payload = {
'from' : '/bbs/Gossiping/index.html',
'yes' : 'yes'
}
rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
#res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
print (res.text)


# In[ ]:



