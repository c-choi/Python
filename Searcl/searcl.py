# creating multi-threading (multi worker) / queue = work
import threading
# import string
from queue import Queue
from spider import Spider
from domain import *
from general import *
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from naver_api import cwd, search_word
from datetime import datetime

today = str(datetime.date(datetime.now()))

PROJECT_NAME = today + "/" + search_word
with open(cwd + "/" + PROJECT_NAME + "/queue.txt", 'r') as f:
    j = f.readlines()
    i = 0
    if len(j) == 0:
        print("검색결과가 " + str(len(j)) + "건 입니다.")
        raise SystemExit

    while i < len(j):
        HOMEPAGE = j[i].strip("\n")
        DOMAIN_NAME = get_domain_name(HOMEPAGE)
        i += 1

    # First Thread completed, gathered links in homepage, created txt files from the first page
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'  # cwd + '/queue.txt'  #
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'  # cwd + '/crawled.txt' #
    # limiting number of threads that the computer (OS) can handle
    NUMBER_OF_THREADS = 8
    queue = Queue()


# Multi-thread -> Create worker threads (will die when main exits) / '_' = disregarding value in any range (don't matter so much)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        # ensuring this works under daemon process and dies after main exits
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        # take links from queue.txt to create_jobs
        queue.put(link)
    queue.join()
    crawl()


# check if there are items in the queue, if so crawl them
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()


def urlib(full_link):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    req = Request(full_link, headers=headers)
    try:
        resp = urlopen(req)
        respData = resp.read()
        soup = BeautifulSoup(respData, "lxml")
        # print(soup.link)
        s = soup.p
        # TODO: HTML안에서 서치워드 찾아내서 문장 찾아오기
        for paragraph in s:
            lines = paragraph.split(".")
            for each_line in lines:
                if not each_line.find(search_word) > 0:
                   pass

                    # soup.get_text(search_word)
                    # text = text + str(item.find_all(text=True))
    except Exception as e:
        # print(e)
        pass


with open(cwd + "/" + PROJECT_NAME + "/crawled.txt", 'r') as g:
    h = g.readlines()
    j = 0
    for i in h:
        urlib(h[j])
        j += 1
