import scrapy

class RTItem(scrapy.Item):
     title = scrapy.Field()
     score = scrapy.Field()
     genres = scrapy.Field()
     consensus = scrapy.Field()
