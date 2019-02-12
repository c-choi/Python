
# coding: utf-8

# # 광고 통계
#
# <img src="https://i.imgur.com/tU3PnSZ.png" >
#
# ##### 2018 FinanceData.KR

# # 광고주 광고비
#
# https://www.adic.or.kr/stat/main/getStats.do?className=AdvertiserAdOutlay
#
# * 월별 100대 광고주의 4대 매체 광고비 현황 (닐슨코리아) (단위:천원)
# * 기간: 1995년 1월~ 현재

# In[1]:


import requests
import json

url = 'https://www.adic.or.kr/stat/periodicalStat/list.json'
data = {
    'className':'AdvertiserAdOutlay',
    'syear':'2018',
    'smonth':'4',
}
r = requests.post(url, data)
json_text = r.text
json_text[:1000]


# In[2]:


import pandas as pd
from pandas.io.json import json_normalize

jo = json.loads(json_text)
df = json_normalize(jo, 'resultList')
print(len(df))
df.head(20)


# In[3]:


# 광고주 광고비
# 월별 100대 광고주

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

def advertiser_ad_outlay(year, month):
    url = 'https://www.adic.or.kr/stat/periodicalStat/list.json'
    data = {
        'className':'AdvertiserAdOutlay',
        'syear': str(year),
        'smonth': str(month),
    }
    r = requests.post(url, data)
    jo = json.loads(r.text)
    df = json_normalize(jo, 'resultList')
    return df


# In[4]:


advertiser_ad_outlay(1996, 1).head(20)


# # 업종별 광고비
# 월별, 21개 업종 구분별 광고비 및 총계
#
# https://www.adic.or.kr/stat/main/getStats.do?className=IndustryAdOutlay

# In[5]:


# 업종별광고비

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

def industry_ad_outlay(year, month):
    url = 'https://www.adic.or.kr/stat/periodicalStat/list.json'
    data = {
        'className':'IndustryAdOutlay',
        'syear': str(year),
        'smonth': str(month),
    }
    r = requests.post(url, data)
    jo = json.loads(r.text)
    df = json_normalize(jo, 'resultList')
    return df


# In[6]:


df = industry_ad_outlay(2018, 1)
df


# In[7]:


df['name'].values


#
#
# #### 2018 FinanceData.KR [facebook.com/financedata](http://facebook.com/financedata)