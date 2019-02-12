# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import os
import csv

today = str(datetime.date(datetime.now()))
time = str(datetime.timestamp(datetime.now()))
cwd = os.getcwd()
project_name = "NEMO Smart Factory"

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# try:
#     # chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#     # Windows headless Chrome
#     # driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe', chrome_options=chrome_options)
#     # driver = webdriver.Chrome('C:/Users/Admin/Dropbox/Nemo IEG/Python/chromedriver.exe')
#     driver = webdriver.Firefox()
# except:
#
#     # chrome_options.binary_location = '/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver'
#     # # driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver', chrome_options=chrome_options)
#     # driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
#     driver = webdriver.Firefox()

# driver = webdriver.Firefox()
driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')

def write_csv(data):
    if not os.path.exists(cwd + "/" + project_name):
        try:
            os.makedirs(cwd + "/" + project_name)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
    csv_f = open(srcFile, 'w', encoding='euc_kr', newline='')
    wr = csv.writer(csv_f)
    for a in data:
        wr.writerow(a)


def get_company():
    url = "https://www.smart-factory.kr/buzInfo/authComp.do#this"
    # url = "https://www.naver.com"
    driver.get(url)
    file_data = []
    file_header = []

    for i in range(0, 3):

        if i != 0:
            next_page()

        table = driver.find_element_by_class_name('q_table03')
        head = table.find_element_by_tag_name('thead')
        body = table.find_element_by_tag_name('tbody')

        if i == 0:
            head_line = head.find_element_by_tag_name('tr')
            headers = head_line.find_elements_by_tag_name('th')
            for header in headers:
                header_text = header.text
                file_header.append(header_text)
            file_data.append(file_header)

        body_rows = body.find_elements_by_tag_name('tr')
        for row in body_rows:
            data = row.find_elements_by_tag_name('td')
            # id = data.get_attribute('href')
            # print(id)
            file_row = []
            for datum in data:
                datum_text = datum.text
                file_row.append(datum_text)
            file_data.append(file_row)
    write_csv(file_data)

def next_page():
    driver.find_element_by_xpath('//*[@id="PAGE_NAVI"]/a[13]/img').click()
    driver.implicitly_wait(3)

srcFile = cwd + "/" + project_name + "/" + str(datetime.today()) + ".csv"
get_company()


# write_csv()
