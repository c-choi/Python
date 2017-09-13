# use html parser to find html class (a)

from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # HTMLparser function to find all the html start tags -> find only 'a' tags
    # attribute = class, id, href ...
    # finder = LinkFinder()
    # finder.feed('<html><head><title>Test</title></head>'
    #             '<body><h1>Parse me!</h1></body></html>') -> what parser does
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
