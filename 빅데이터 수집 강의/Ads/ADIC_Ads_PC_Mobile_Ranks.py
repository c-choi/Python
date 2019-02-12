# coding: utf-8

# # 광고 통계 - PC도메인 모바일 앱 이용순위
#
# <img src="https://i.imgur.com/tU3PnSZ.png" >
#
# ##### 2018 FinanceData.KR

# # PC 도메인 이용순위
#
# https://www.adic.or.kr/stat/main/getStats.do?className=PcDomain
#
# * 월별 PC도메인 이용순위(순방문자 기준)
# * 2014년 11월 ~ 현재

# In[1]:


# PC 도메인 이용순위

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


def pc_domain(year, month):
    url = 'https://www.adic.or.kr/stat/periodicalStat/list.json'
    data = {
        'className': 'PcDomain',
        'syear': year,
        'smonth': month,
    }
    r = requests.post(url, data)
    jo = json.loads(r.text)
    df = json_normalize(jo, 'resultList')
    return df


# In[2]:


pc_domain(2017, 1)

# In[3]:


import pandas as pd

dt_range = pd.date_range('2014-11-01', '2018-06-01', freq='MS')
dt_range

# In[4]:


df_list = []
for dt in pd.date_range('2014-11-01', '2018-06-01', freq='MS'):
    df = pc_domain(dt.year, dt.month)
    df['date'] = dt
    df_list.append(df)

df_domain = pd.concat(df_list, sort=True)
df_domain.head()

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (14, 6)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True

# In[7]:


df = pd.pivot_table(df_domain, values='visitor', index='date', columns='name')
df[['naver.com', 'daum.net', 'google.com', 'youtube.com']].plot()

# In[8]:


df[['naver.com', 'daum.net', 'google.com', 'youtube.com']].plot(secondary_y=['google.com', 'youtube.com'])

# In[9]:


df[['11st.co.kr', 'gmarket.co.kr']].plot()

# # 모바일 앱 이용순위
#
# 안드로이드 운영체제 기준
#
# https://www.adic.or.kr/stat/main/getStats.do?className=PcDomain

# In[11]:


# Moblie 앱 이용순위

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


def mobile_app(year, month):
    url = 'https://www.adic.or.kr/stat/periodicalStat/list.json'
    data = {
        'className': 'MoblieApp',
        'syear': str(year),
        'smonth': str(month),
    }
    r = requests.post(url, data)
    jo = json.loads(r.text)
    df = json_normalize(jo, 'resultList')
    return df


# In[12]:


mobile_app(2018, 1)

# # Quiz
# * 모바일 앱(현재, 상위 5개)의 사용 순위 변화를 차트로 표현

#
#
# #### 2018 FinanceData.KR [facebook.com/financedata](http://facebook.com/financedata)