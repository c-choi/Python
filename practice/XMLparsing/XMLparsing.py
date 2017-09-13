from bs4 import BeautifulSoup

# soup = BeautifulSoup(books_xml, "lxml")
# # parsing file = books_xml, parser = lxml
#
# soup.find_all("author")
# # 해당 패턴 모두 반환
#
# find("invention-title")
#
# get_text():
# # 반환된 패턴의 값 반환 (태그와 태그 사이)


# from bs4 import BeautifulSoup
#
# with open("books.xml", "r", encoding="utf8") as books_file:
#     books_xml = books_file.read() # 파일을 스트링으로 읽어오기
#
# soup = BeautifulSoup(books_xml, 'lxml') #lxml Parser 사용하여 데이터분석
#
# # author가 들어간 모든 elememt 추출
# for book_info in soup.find_all("author"):
#     print(book_info)
#     print(book_info.get_text())

import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.XML", "r", encoding="utf8") as patent_xml:
    xml = patent_xml.read()

soup = BeautifulSoup(xml, "lxml")

invention_title_tag = soup.find("invention-title")
print(invention_title_tag.get_text())

publication_reference_tag = soup.find("publication-reference")
p_document_id_tag = publication_reference_tag.find("document-id")
p_country = p_document_id_tag.find("country").get_text()
p_doc_number = p_document_id_tag.find("doc-number").get_text()
p_kind = p_document_id_tag.find("kind").get_text()
p_date = p_document_id_tag.find("date").get_text()

print(p_country, p_doc_number, p_kind, p_date)

application_reference_tag = soup.find("application-reference")
a_document_id_tag = application_reference_tag.find("document-id")
a_country = a_document_id_tag.find("country").get_text()
a_doc_number = a_document_id_tag.find("doc-number").get_text()
a_date = a_document_id_tag.find("date").get_text()

print(a_country, a_doc_number, a_date)