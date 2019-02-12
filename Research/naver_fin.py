# -*- coding: utf-8 -*-
import re
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

today = str(datetime.date(datetime.now()))
time = str(datetime.timestamp(datetime.now()))
cwd = os.getcwd()
project_name = "NEXEN" #input()
try:
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
except:
    font_name = font_manager.FontProperties(fname="/Library/Fonts/NanumBarunGothic.otf").get_name()
    rc('font', family=font_name)


def write_csv():
    if not os.path.exists(cwd + "/" + project_name):
        try:
            os.makedirs(cwd + "/" + project_name)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

    df.to_csv(cwd + "/" + project_name + "/" + today + " "+ code_type + "[" + code + "]" + '.csv')

def get_header_str(s):
    header_str = ''
    hangul = re.compile('[^ ㄱ-ㅣ가-힣A-Za-z()%]+')
    result = hangul.sub('', s[0])
    header_str = result
    return header_str

'''
get_date_str(s) - 문자열 s 에서 "YYYY/MM" 문자열 추출
'''
def get_date_str(s):
    date_str = ''
    # print(s)
    r = re.search("\d{4}/\d{2}", s[1])
    if r:
        date_str = r.group()
        date_str = date_str.replace('/', '-')
        date_str = date_str.replace(date_str[:4],str(int(date_str[:4])-1))
    return date_str

'''
* code: 종목코드
* fin_type = '0': 재무제표 종류 (0: 주재무제표, 1: GAAP개별, 2: GAAP연결, 3: IFRS별도, 4:IFRS연결)
* freq_type = 'Y': 기간 (Y:년, Q:분기)
'''
def get_finstate_naver(code, fin_type='0', freq_type='Y'):
    url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?' \
                   'cmp_cd=%s&fin_typ=%s&freq_typ=%s'

    url = url_tmpl % (code, fin_type, freq_type)
    print(url)
    dfs = pd.read_html(url, encoding="utf-8")
    df = dfs[0]
    if df.ix[0, 0].find('해당 데이터가 존재하지 않습니다') >= 0:
        return None
    df.rename(columns={'주요재무정보':'date'}, inplace=True)
    # print(df)
    df.set_index('date', inplace=True)
    # df.head
    cols = list(df.columns)

    if '연간' in cols: cols.remove('연간')
    if '분기' in cols: cols.remove('분기')

    cols = [get_date_str(x) for x in cols]
    cols.pop()

## TODO: header 한칸 밀기
    df = df.ix[:, :-1]
    df.columns = cols
    dft = df.T
    index = [get_header_str(x) for x in dft.columns]
    dft.columns = index
    dft.index = pd.to_datetime(dft.index)
    # remove if index is NaT
    dft = dft[pd.notnull(dft.index)]
    return dft


def get_code(input):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    url = 'http://finance.naver.com/'
    #
    try:
        chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        # Windows headless Chrome
        driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe', chrome_options=chrome_options)
        # driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe')
        driver.get(url)
    except:

        chrome_options.binary_location = '/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver'
        # # driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver', chrome_options=chrome_options)
        driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
        #
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="stock_items"]').send_keys(code_type)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/button').click()
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]')

        print(driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]').text)
        try:
            names = driver.find_elements_by_class_name('tit')
            for n in range(len(names)):
                print(names[n].text)
            try:
                name = code_type
            except:
                name = names[0].text
            print(name)
            driver.find_element_by_link_text(name).click()
            code = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]').text
        except:
            print("데이터가 없습니다")
            exit()
    except:
        try:
            names = driver.find_elements_by_class_name('tit')
            for n in range(len(names)):
                print(names[n].text)
            try:
                name = code_type
            except:
                name = names[0].text
            print(name)
            driver.find_element_by_link_text(name).click()
            code = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]').text
        except:
            print("데이터가 없습니다")
            exit()

    return code

code_type = input("회사명을 입력해주세요\n")
code = get_code(code_type)
print(code_type, code)
df = get_finstate_naver(code)


print(df[['매출액', '영업이익', '당기순이익', '영업활동현금흐름', '순이익률', 'ROE(%)', 'ROA(%)', '부채비율', '자본유보율', 'EPS(원)', 'PER(배)', 'BPS(원)', 'PBR(배)']])
write_csv()

df[['매출액', '영업이익', '당기순이익', '영업활동현금흐름', '순이익률', 'ROE(%)', 'ROA(%)', '부채비율', '자본유보율', 'EPS(원)', 'PER(배)', 'BPS(원)', 'PBR(배)']].plot()
plt.show()


