import csv
import os
from datetime import datetime
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

today = str(datetime.date(datetime.now()))
time = str(datetime.timestamp(datetime.now()))
cwd = os.getcwd()
project_name = "쇼핑인사이트" #input()
csv_file = str(today + "_ShoppingRank.csv")

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument('disable-gpu')
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR") # 한국어!
#
# driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver = webdriver.Firefox()

# driver = webdriver.PhantomJS('/Users/cloudy/anaconda/bin/phantomjs')
# try:
    # Windows headless Chrome
    # driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe', chrome_options=chrome_options)
    # driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe')
# except:
#     driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
def list_up():
    driver.implicitly_wait(3)
    # 데이터랩 페이지 열기
    driver.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
    # 연령대 설정
    driver.find_element_by_xpath('//*[@id="20_age_2"]').click()
    driver.find_element_by_xpath('//*[@id="20_age_3"]').click()
    category = {}
    # First dropdown list
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
    first_ul_list = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul')
    first_list_items = [li.text for li in first_ul_list.find_elements_by_tag_name('li')]
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
    # print(first_list_items)
    for g in range(0, len(first_list_items)):
        driver.implicitly_wait(3)
        # loop through first dropdown
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
        first = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[' + str(g + 1) + ']').text
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[' + str(g + 1) + ']').click()
        # print(first)
        # Second dropdown list
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/span').click()
        second_ul_list = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/ul')
        second_list_items = [li.text for li in second_ul_list.find_elements_by_tag_name('li')]
        # print(second_list_items)
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/span').click()
        # Second dropdown loop
        second_category = {}
        wait = WebDriverWait(driver, 10)
        for h in range(0, len(second_list_items)):
            driver.implicitly_wait(30)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > h4 > strong')))
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/span').click()
            # Second dropdown list click
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/ul/li[' + str(h + 1) + ']').click()
            except:
                continue
            driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a/span').click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                       '#chart1 > svg > g:nth-child(2) > g.c3-chart > g.c3-event-rects.c3-event-rects-single > rect.c3-event-rect.c3-event-rect-31')))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > h4 > strong')))
            list = []
            for j in range(0, 5):
                try:
                    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/span').click()
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/span').click()
                except:
                    continue

                # check if rank list is refreshed
                check = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/a/span').text
                while int(check) != int(j*20 + 1):
                    print(str(check) + " " + str(j*20+1))
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > div > div.rank_top1000_scroll > ul > li:nth-child(1) > a > span')))
                    # 번호 바뀌었는지 재확인
                    check = driver.find_element_by_xpath(
                        '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/a/span').text
                    if int(check) < int(j*20 + 1):
                        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
                    elif int (check) > int(j*20 + 1):
                        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[1]').click()

                driver.implicitly_wait(10)
                for i in range(1, 21):
                    item = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[' + str(i) + ']/a').text.replace("\n", "")
                    list.append(item)
                driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
                try:
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > div > div.rank_top1000_scroll > ul > li:nth-child(1) > a > span')))
                except:
                    continue
                driver.implicitly_wait(3)
                # driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/a/span').click()
            # Get Second category name
            name = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/h4/strong').text
            print(h + 1, first, name)

            # print(list)
            second_category[name] = list
        # pprint(second_category)
        category[first] = second_category
        pprint(str(first) + " " + str(second_category))
    pprint(category)
    write_csv(category)

def write_csv(category):
    # Check if folder exists
    if not os.path.exists(cwd + "/" + project_name + "/" + today):
        try:
            os.makedirs(cwd + "/" + project_name + "/" + today)
        except OSError as error:
            if error.errno != error.errno.EEXIST:
                raise
    # write data for csv
    comp_data = open(cwd + "/" + project_name + "/" + today + "/" + csv_file, 'a',
                     encoding='utf-16', newline='')
    csvwriter = csv.writer(comp_data, delimiter="\t")
    # Loop to write data to file
    for f, s in category.items():
        for k, v in s.items():
            for n in range(0, len(v)):
                csvwriter.writerow([n + 1] + [f] + [k] + [v[n].replace(str(n+1),"")])

# os.system("start excel.exe %s" %cwd + "\\" + project_name + "\\" + today + "\\" + csv_file)

list_up()
driver.quit()