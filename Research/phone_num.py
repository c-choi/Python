import requests
from bs4 import  BeautifulSoup

url = 'http://www.isuperpage.co.kr/search.asp'
searchword = input("검색어를 입력해주세요\n")

data = {
    'searchWord': searchword.encode('euc-kr'),
    'dong':''.encode('euc-kr'),
    'city': '서울'.encode('euc-kr'),
    'gu': ''.encode('euc-kr'),
}

r = requests.post(url, data=data)
r.text[:1000]

soup = BeautifulSoup(r.text, 'lxml')
search_result = soup.find('div', {'id':'search_result'})

lis = search_result.find_all('li')[2:]
for li in lis:
    divs = li.find_all('div')

    # div[0]
    title = divs[0].a.text # 상호
    spans = divs[0].find_all('span')
    search = spans[1].text # 검색어

    # div[1]
    spans = divs[1].find_all('span')
    # print(spans)
    phone = spans[0].text # 전화번호
    addr = spans[1].text  # 주소
    addr_road = spans[3].text  # 도로명 주소

    print( "%s, %s, %s, %s, %s" % (title, search, phone, addr, addr_road))