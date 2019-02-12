# -*- coding:utf-8 -*-
import openpyxl
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import csv
import re
from pprint import pprint
from time import sleep

options = Options()
prefs = {
    "plugins.plugins_enabled": 'Adobe Flash Player',
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls" : "https://sminfo.mss.go.kr/"
}
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("proxy-server=localhost:8080")

options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver', options=options)


# driver = webdriver.Chrome('chromedriver', options=options)
wait = WebDriverWait(driver, 10)

today = str(datetime.date(datetime.now()))
cwd = os.getcwd()
project_name = "NEMO"  # input()
csv_file = str(today + ".csv")


def scrap(searchid):
    cpdict = {}
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div[3]/table/tbody')))
    num = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/p[1]/strong/span').text
    print("검색결과 : " + num + "건")
    page = str(int(num.replace(',', ''))//10 + 1)

    if num == 0:
        return
    if num == 1:
        cptitle = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[1]/a/strong')
        ceo = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[2]')
        cptype = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[3]')
        cpprod = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[4]')
        cpaddress = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[5]')
        cpid = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr/td[1]/a').get_attribute('onclick')
        reid = re.findall("(\d{10})", cpid)
        cpdict[reid[0]] = ([cptitle.text, ceo.text, cptype.text, cpprod.text, cpaddress.text])

    else:
        for i in range(1, 11):
            try:
                cptitle = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr['+ str(i) + ']/td[1]/a/strong')
                ceo = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr[' + str(i)+ ']/td[2]')
                cptype = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr[' + str(i)+ ']/td[3]')
                cpprod = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr[' + str(i) + ']/td[4]')
                cpaddress = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr[' + str(i)+ ']/td[5]')
                cpid = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/table/tbody/tr['+ str(i) + ']/td[1]/a').get_attribute('onclick')
                reid = re.findall("(\d{10})", cpid)
                cpdict[reid[0]] = ([cptitle.text, ceo.text, cptype.text, cpprod.text, cpaddress.text])
            except:
                break
    pprint(cpdict)

    searchkey = list(cpdict)
    print(searchkey[0])
    searchid = searchkey[0]
    print(searchid + "에 대한 매출 정보를 검색합니다")
    cpinfo(searchid)

def cpinfo(searchid):
    driver.execute_script("javascript:onMoveView01('" + searchid + "'); return false;")
    cptitle = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]').text
    ceo = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]').text
    cptype = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[1]').text
    cpdate = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]').text
    cpadd = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[4]/td').text
    cphp = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[1]').text
    cpprod = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]').text
    cpind = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[1]').text
    driver.find_element_by_xpath('//*[@id="TabCoinfo"]/li[5]/a').click()

    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        return
    print("test")
    salesheader = []
    sales = []
    sales2 = []
    for i in range(1, 8):
        try:
            salesheader.append(driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/thead/tr/th[' + str(i) + ']').text)
            sales.append(driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[1]/td['+ str(i) + ']').text)
            sales2.append(driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/table/tbody/tr[2]/td['+ str(i) + ']').text)
        except:
            continue
    try:
        data = [cptitle, ceo, cptype, cpdate, cpadd, cphp, cpprod, cpind, sales[0], sales[1],sales[2], sales[3], sales[4], sales[5], sales[6]]
        print(data)
    except:
        print("매출 정보가 없습니다.")
        return
    csv_data = { str(searchid) : data}
    pprint(csv_data)
    # write_csv(csv_data, cptitle)

def write_csv(cpdict, cpname):
    if not os.path.exists(cwd + "/" + project_name + "/" + today):
        try:
            os.makedirs(cwd + "/" + project_name + "/" + today)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
    columns = ['ID', '회사명', '대표자', '기업형태', '설립일자', '주소', '홈페이지','제조품목', '표준산업', '결산년도', '총자산', '납입자본금', '자본총계', '매출액', '영업이익', '당기순이익']
    comp_data = open(cwd + "/" + project_name + "/" + today + "/" + csv_file, 'a',
                     encoding='utf-16', newline='')
    csvwriter = csv.writer(comp_data, delimiter="\t")
    csvwriter.writerow(columns)

    for k, v in cpdict.items():
        csvwriter.writerow([k] + v)
        for b in range(1, len(colB)):
                if colB[b].value == v[1]:
                    print("TEST")
                    for n in range(1, 15):
                        print(a, n, v[n])
                        # ws_cell(row=a, col=n).value = v[n]
                        ws.cell(row=a, column=n, value=v[n])
                    wb.save(cwd + "/" + project_name + "/" + today + "/" + "Company_Research.xlsx")
    # os.system("start excel.exe %s" %cwd + "\\" + project_name + "\\" + today + "\\" + csv_file)
    return cpdict

def clist(compname):
    cpname = compname #input('회사명을 입력해주세요\n')

    print(cpname)
    actions = ActionChains(driver)
    menu = driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/div/a/img')
    actions.move_to_element(menu).perform()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#header > div > div.menu > ul > li.m1 > div > a')))
    driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/ul/li[1]/a').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="searchTxt"]').send_keys(cpname)
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/fieldset/div[2]/p/input').click()

    for g in range(1, 10):
        comp_data = scrap(compname)
        try:
            driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[3]/p/a[' + str(g) + ']').click()
        except:
            break
        return comp_data


driver.implicitly_wait(3)
driver.get('https://sminfo.mss.go.kr/')
original = driver.current_window_handle
original_name = original.title()
window_num = len(driver.window_handles)

driver.find_element_by_name('login_id').send_keys('cchoi1989')
driver.find_element_by_name('login_password').send_keys("CcPs4141@@")
driver.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/div/input').click()

for i in range(1, window_num + 3):
    try:
        driver.switch_to.window(driver.window_handles[i])
        current_window = driver.window_handles[i]
        if current_window.upper() != original_name.upper():
            driver.close()
    except:
        i = 1

driver.switch_to.window(original)
#'1018142433', '1048141995', '1048199352', '1058156720', '1058193517', '1058611499', '1058672026', '1058723347', '1058727362', '1058741568', '1058763183','1058773702','1068178464','1068626016','1068634670','1068638166','1078132947','1078611215','1078618241','1078635726',
complist = ['1078639760', '1078649157', '1078729987', '1078750855', '1078776928', '1078803970', '1088167100', '1088172578', '1098161434', '1098637958', '1100275030', '1138135478', '1138603670', '1138608689', '1138616200', '1138622003', '1138666433', '1138670956', '1138691698', '1148163002', '1148604139', '1148638736', '1148647351', '1148650569', '1148691478', '1168119273', '1168124039', '1168136267', '1178122859', '1178154123', '1188106338', '1188117174', '1190436950', '1198141283', '1198146217', '1198162575', '1198169165', '1198172132', '1198181382', '1198185224', '1198185767', '1198188750', '1198193350', '1198194626', '1198604089', '1198627286', '1198628548', '1198645120', '1198645625', '1198646115', '1198653294', '1198658950', '1198659420', '1198661187', '1198684180', '1198705616', '1208110951', '1208170885', '1208183022', '1208184846', '1208600841', '1208620788', '1208627419', '1208638987', '1208641236', '1208670779', '1208701814', '1208706032', '1208734182', '1208741456', '1208749934', '1218606964', '1222848900', '1228192610', '1238148548', '1238151422', '1238610839', '1238637537', '1244956721', '1248638387', '1248660822', '1248704943', '1258199913', '1288145207', '1288194275', '1288663928', '1298124393', '1298136924', '1298156556', '1298172861', '1298195428', '1298661715', '1308172560', '1308609441', '1308625742', '1308683378', '1318176647', '1318179251', '1318186072', '1318189759', '1348108473', '1348160260', '1348652839', '1358155834', '1358161199', '1358192256', '1358606250', '1388138998', '1388171717', '1408111518', '1408161814', '1420841373', '1438110177', '1448105570', '1448136210', '1480500724', '1948100551', '2018121664', '2018122611', '2018160779', '2038164392', '2048137812', '2048162719', '2068124083', '2068186323', '2068188807', '2068668219', '2068672289', '2068701291', '2088106344', '2098156056', '2118710133', '2118726329', '2118815611', '2138626482', '2148640930', '2148685446', '2148714220', '2158186384', '2158603016', '2158637423', '2158653175', '2158723455', '2178136065', '2178145128', '2198100428', '2198130368', '2208119816', '2208123474', '2208174745', '2208185145', '2208193121', '2208632304', '2208658565', '2208704576', '2208715414', '2208838578', '2298101254', '2298122827', '2468700397', '2558700391', '2648148780', '2668100045', '2738100742', '3018152448', '3058170583', '3058173988', '3058605020', '3091761197', '3128636894', '3148114800', '3148116865', '3148134223', '3148160435', '3148177203', '3148179477', '3148182050', '3148645797', '3178124118', '4028151311', '4098186960', '4098637066', '4108168846', '4108192588', '4108600837', '4188148029', '4248800499', '4598700386', '5028141767', '5028154675', '5028186779', '5028605067', '5028638802', '5031265015', '5038151220', '5038166460', '5038185074', '5038611276', '5038616102', '5041639987', '5048119960', '5048144440', '5048145833', '5048147317', '5048170045', '5058167029', '5131745952', '5131816702', '5138141845', '5148148633', '5158131630', '5158149988', '5658500289', '6058164185', '6068159313', '6068164999', '6068181095', '6068185320', '6068608105', '6068634525', '6078165220', '6078180158', '6088199892', '6092486607', '6098132666', '6098137448', '6098142941', '6098148886', '6098172708', '6098176271', '6098190161', '6098532761', '6108123231', '6108613761', '6108614101', '6108625272', '6158116939', '6158130872', '6178183910', '6178191045', '6178614723', '6178617808', '6188108291', '6208125459', '6211030218', '6218128691', '6218138151', '6218172412', '6218191234', '6418600708', '6688100620', '7548700132', '8638600614']

for compname in complist:
    clist(compname)
    print("Sleeping")
    sleep(60)