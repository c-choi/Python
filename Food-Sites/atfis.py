from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

comp_name = input("회사명을 입력해주세요: ")
keyword = input("검색어를 입력해주세요: ")

url = 'https://www.atfis.or.kr/business/M002040000/list.do?searchTopIndustry=ALL&searchKeyIndicators=S' \
      '&searchKeyIndicators=E&searchKeyIndicators=N&businessOpen=001&_businessOpen=on&businessOpen=002' \
      '&_businessOpen=on&businessOpen=003&_businessOpen=on&businessOpen=004&_businessOpen=on&businessOpen=005' \
      '&_businessOpen=on&_businessOpen=on&sortOrderBy=S_DESC&searchMinYear=2016&searchMaxYear=2016&recordCount=100' \
      '&searchBusinessNm=' + str(comp_name) + '&searchProductItem=' + str(keyword) \
      + '&x=0&y=0'

driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
driver.get(url)

driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lists = soup.find_all("table", {"class": "table_view2"})
# try:
data = lists[0].find_all("td", {"class": "ellipsis"})
dic = {}
for i in range(len(data)):
    text = data[i ].text.strip()
    # try:
    #     dic[title].append(text)
    # except:
    #     dic[title] = text
    print(text)
print("-" * 100)

# except:
#     print("0 results")
# original = driver.current_window_handle
# original_name = original.title()
# window_num = len(driver.window_handles)
#
# driver.find_element_by_name('login_id').send_keys('cchoi1989')
# driver.find_element_by_name('login_password').send_keys("CcPs4141")
# driver.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/div/input').click()
#
# for i in range(1, window_num + 1):
#     try:
#         driver.switch_to.window(driver.window_handles[i])
#         current_window = driver.window_handles[i]
#         print(current_window.upper() + " " + original_name.upper())
#         if current_window.upper() != original_name.upper():
#             driver.close()
#     except:
#         continue
#
# driver.switch_to.window(original)
#
# wait = WebDriverWait(driver, 10)
# actions = ActionChains(driver)
# menu = driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/div/a/img')
# actions.move_to_element(menu).perform()
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#header > div > div.menu > ul > li.m1 > div > a')))
# driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/ul/li[1]/a').click()
#
# driver.implicitly_wait(3)
# cpname = input('회사명을 입력해주세요\n')
# # cpname = "네모아이이지"
# driver.find_element_by_xpath('//*[@id="searchTxt"]').send_keys(cpname)
# driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/fieldset/div[2]/p/input').click()
