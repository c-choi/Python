
# coding: utf-8

# # FinanceDataReader 사용자 안내서
#
# <img src="https://i.imgur.com/r0YE5Xs.png">
#
# 한국 주식 가격, 미국주식 가격, 지수, 환율, 암호화폐 가격, 종목 리스팅 등 금융 데이터 수집 라이브러리
#
# <!-- TEASER_END -->
# ### 2018 FinanceData.KR

# In[9]:


#  차트 설정
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True


# # 개요
#
# 금융 데이터를 다루는데 가장 기본이 되는 데이터는 거래소별 전체 종목 코드와 가격 데이터 이다.
#
# [pandas-datareader](https://pandas-datareader.readthedocs.io) 는 잘 구성된 시계열 데이터 수집 라이브러리로 사용이 간편하고 다양한 시계열 데이터를 수집할 수 있다는 장점이 있다.  (현재 버전 : pandas_datareader 0.6.0) 하지만, 거래소별(KRX, NASDAQ, NYSE 등) 전체 종목 코드(ticker symbol)를 가져오는 기능이 없으며, 야후 파이낸스가 더 이상지원되지 않고(deprecated), 구글 파이낸스는 UNSTABLE_WARNING + RemoteDataError 를 낸다.
#
# FinanceDataReader는 [pandas-datareader](https://pandas-datareader.readthedocs.io) 를 대체하기 보다 보완하기 위한 목적으로 만들어졌다. 주요한 기능은 다음과 같다.
#
# ### 종목 코드
# * 거래소별 전체 종목코드: KRX (KOSPI, KODAQ, KONEX), NASDAQ, NYSE, AMEX, S&P 500
#
# ### 가격 데이터
# * 해외주식 가격 데이터: AAPL(애플), AMZN(아마존), GOOG(구글) 등
# * 국내주식 가격 데이터: 005930(삼성전자), 091990(셀트리온헬스케어) 등
# * 각종 지수: KS11(코스피지수), KQ11(코스닥지수), DJI(다우지수), IXIC(나스닥 지수), US500(S&P 5000)
# * 환율 데이터: USD/KRX (원달러 환율), USD/EUR(달러당 유로화 환율), CNY/KRW: 위엔화 원화 환율
# * 암호화폐 가격: BTC/USD (비트코인 달러 가격, Bitfinex), BTC/KRW (비트코인 원화 가격, 빗썸)
#

# # 설치
#
# ```bash
# pip install -U finance_datareader
# ```

# # 사용

# In[2]:


import FinanceDataReader as fdr
fdr.__version__


# # 전체 종목 코드
# 종목 데이터 전체를 얻기 위해 사용할 수 있는 거래소 심볼은 다음과 같다
#
# ### 한국
#
# 심볼 | 거래소
# --------|---------
# KRX | KRX 종목 전체
# KOSPI | KOSPI 종목
# KOSDAQ  | KOSDAQ 종목
# KONEX  | KONEX 종목
#
#
# ### 미국
# 심볼 | 거래소 |
# --------|---------
# NASDAQ | 나스닥 종목
# NYSE  |뉴욕 증권거래소 종목
# AMEX  | AMEX 종목
# SP500 | S&P 500 종목
#
#
# ※ KRX는 KOSPI,KOSDAQ,KONEX 모두 포함

# In[3]:


import FinanceDataReader as fdr

# 한국거래소 상장종목 전체
df_krx = fdr.StockListing('KRX')
df_krx.head()


# In[4]:


len(df_krx)


# In[5]:


import FinanceDataReader as fdr

# S&P 500 종목 전체
df_spx = fdr.StockListing('S&P500')
df_spx.head()


# In[6]:


len(df_spx)


# # 가격 데이터 - 국내주식
# 단축 코드(6자리)를 사용.
#
# * 코스피 종목: 068270(셀트리온), 005380(현대차)  등
# * 코스닥 종목: 215600(신라젠), 151910(나노스) 등

# In[7]:


import FinanceDataReader as fdr

# 신라젠, 2018년
df = fdr.DataReader('215600', '2018-01-01')
df.head(10)


# In[10]:


import FinanceDataReader as fdr

# 셀트리온, 2017년~현재
df = fdr.DataReader('068270', '2017-01-01')
df['Close'].plot()


# # 가격 데이터 - 미국 주식
# 티커를 사용. 예를 들어, 'AAPL'(애플), 'AMZN'(아마존), 'GOOG'(구글)

# In[11]:


import FinanceDataReader as fdr

# 애플(AAPL), 2018-01-01 ~ 2018-03-30
df = fdr.DataReader('AAPL', '2018-01-01', '2018-03-30')
df.tail()


# In[12]:


import FinanceDataReader as fdr

# 애플(AAPL), 2017년
df = fdr.DataReader('AAPL', '2017')
df['Close'].plot()


# In[13]:


import FinanceDataReader as fdr

# 아마존(AMZN), 2010~현재
df = fdr.DataReader('AMZN', '2010')
df['Close'].plot()


# # 한국 지수
# 심볼 | 설명
# ---------- | ---------------
# KS11 | KOSPI 지수
# KQ11 | KOSDAQ 지수
# KS50 | KOSPI 50 지수
# KS100 | KOSPI 100 지수
# KS200 | KOSPI 200 지수
# KRX100 | KRX 100
#

# # 미국 지수
# 심볼 | 설명
# ---------- | ---------------
# DJI | 다우존스 지수
# IXIC | 나스닥 지수
# US500 | S&P 500 지수
# VIX | S&P 500 VIX
#
# ※ DJI, IXIC, US500 가 미국 3대 지수

# # 국가별 주요 지수
# 심볼 | 설명
# ---------- | ---------------
# JP225 | 닛케이 225 선물
# STOXX50 | 유렵 STOXX 50
# HSI | 항셍 (홍콩)
# CSI300 | CSI 300 (중국)
# SSEC |  상해 종합
# UK100 | 영국 FTSE
# DE30 | 독일 DAX 30
# FCHI | 프랑스 CAC 40

# In[14]:


import FinanceDataReader as fdr

# KS11 (KOSPI 지수), 2015년~현재
df = fdr.DataReader('KS11', '2015')
df['Close'].plot()


# In[15]:


# 다우지수, 2015년~현재

df = fdr.DataReader('DJI', '2015')
df['Close'].plot()


# In[16]:


# DAX, 2015년~현재

df = fdr.DataReader('DE30', '2015')
df['Close'].plot()


# # 환율
#
# 심볼 | 설명
# ---------- | ---------------
# USD/KRW | 달러당 원화 환율
# USD/EUR | 달러당 유로화 환율
# USD/JPY | 달러당 엔화 환율
# CNY/KRW | 위엔화 원화 환율
# EUR/USD	| 유로화 달러 환율
# USD/JPY | 달러 엔화 환율
# JPY/KRW	| 엔화 원화 환율
# AUD/USD	| 오스트레일리아 달러 환율
# EUR/JPY	| 유로화 엔화 환율
# USD/RUB	| 달러 루블화

# In[17]:


import FinanceDataReader as fdr

# 원달러 환율, 1995년~현재
df = fdr.DataReader('USD/KRW', '1995')
df['Close'].plot()


# In[18]:


# 위엔화 환율, 1995년~현재

df = fdr.DataReader('CNY/KRW', '1995')
df['Close'].plot()


# # 상품선물
#
# 심볼 | 설명
# ---------- | ---------------
# NG | 천연가스 선물 (NYMEX)
# GC | 금 선물 (COMEX)
# SI | 은 선물 (COMEX)
# HG | 구리 선물 (COMEX)
# CL  | WTI유 선물 (NYMEX)

# In[19]:


import FinanceDataReader as fdr

# 천연가스 선물 (NYMEX)
df = fdr.DataReader('NG', '2018')
df.tail()


# In[20]:


import FinanceDataReader as fdr

# WTI유 선물 (NYMEX)
df = fdr.DataReader('CL', '2018')
df.tail()


# # 채권
# ### 한국
# * 'KR\[년도\]YT=RR' 형식으로 조합 (가능 년도=1,2,3,4,5,10,20,30,50)
#
# 심볼 | 설명
# ---------- | ---------------
# KR1YT=RR | 1년만기 한국 국채 수익률
# KR3YT=RR | 1년만기 한국 국채 수익률
# KR5YT=RR | 5년만기 한국 국채 수익률
# KR10YT=RR | 10년만기 한국 국채 수익률
#
# ### 미국
# * 'US\[개월\]MT=RR' 형식으로 조합 (가능 개월=1,3,6)
# * 'US\[년도\]YT=RR' 형식으로 조합 (가능 년도=1,2,3,4,5,7,10,30)
#
# 심볼 | 설명
# ---------- | ---------------
# US1MT=X | 1개월 미국 국채 수익률
# US6MT=X | 6개월 미국 국채 수익률
# US1YT=X | 1년만기 미국 국채 수익률
# US5YT=X | 5년만기 미국 국채 수익률
# US10YT=X | 10년만기 미국 국채 수익률
# US30YT=X | 30년만기 미국 국채 수익률
#
#

# In[21]:


import FinanceDataReader as fdr

# 10년만기 미국채 수익률
df = fdr.DataReader('US10YT=X', '2018')
df.tail()


# #  암호화폐 가격 (KRW)
# 암호 화폐 원화 가격 (빗썸)
#
# 심볼 | 설명
# ---------- | ---------------
# BTC/KRW | 비트코인 원화 가격
# ETH/KRW | 이더리움 원화 가격
# XRP/KRW | 리플 원화 가격
# BCH/KRW | 비트코인 캐시 원화 가격
# EOS/KRW | 이오스 원화 가격
# LTC/KRW |  라이트 코인 원화 가격
# XLM/KRW | 스텔라 원화 가격

# #  암호화폐 가격 (UDS)
# 암호 화폐 달러화 가격 (Bitfinex)
#
# 심볼 | 설명
# ---------- | ---------------
# BTC/USD | 비트코인 달러 가격
# ETH/USD | 이더리움 달러 가격
# XRP/USD | 리플 달러 가격
# BCH/USD | 비트코인 캐시 달러 가격
# EOS/USD | 이오스 달러 가격
# LTC/USD |  라이트 코인 달러 가격
# XLM/USD | 스텔라 달러 가격

# In[22]:


import FinanceDataReader as fdr

# 비트코인 원화 가격 (빗썸), 2016년~현재
df = fdr.DataReader('BTC/KRW', '2016')
df['Close'].plot()


# In[24]:


import FinanceDataReader as fdr

# 비트코인 USD 가격
df = fdr.DataReader('BTC/USD', '2016')
df['Close'].plot()


# ### 2018 https://fb.com/financedata