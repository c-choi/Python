from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
from bs4 import BeautifulSoup
class Spider:

# class variable to be shared among all instances (spiders) / opened with blank value to be used anytime
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            add_links_to_queue(Spider.gather_links(page_url))
            # moving link from queue to crawled list
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

# converting bytes (0,1) to human readable html code / finder -> object that parses sites
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        # catching server rs & other problems with try method
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                soup = BeautifulSoup(html_bytes, "lxml")
                for each_line in soup:
                    if each_line.find(search_word) > 0:
                        print(each_line)
                    else:
                        pass
                html_string = html_bytes.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url)
            # pass html to parse data
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def update_files():
        # print(Spider.queue)
        # print(Spider.queue_file)
        # print(Spider.crawled)
        # print(Spider.crawled_file)
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)


def add_links_to_queue(links):
    for url in links:
        if url in Spider.queue:
            continue
        if url in Spider.crawled:
            continue
# disable spider from crawling to other domains
    # think how to utilize this line!!!!!!!!!!!!!!!!!!!!!!!!!!
        if Spider.domain_name not in url:
            continue
        Spider.queue.add(url)