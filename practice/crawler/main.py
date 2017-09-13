# creating multi-threading (multi worker) / queue = work
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# Capitalizing code names = constants in Python programming (norm among programmers)
PROJECT_NAME = 'foodmerce'
HOMEPAGE = str('http://www.' + PROJECT_NAME + '.com')
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
# limiting number of threads that the computer (OS) can handle
NUMBER_OF_THREADS = 8
queue = Queue()
# First Thread completed, gathered links in homepage, created txt files from the first page
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


#Multi-thread -> Create worker threads (will die when main exits) / '_' = disregarding value in any range (don't matter so much)
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
