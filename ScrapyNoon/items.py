# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapynoonItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    Name = scrapy.Field()
    Brand = scrapy.Field()
    Average_Rating = scrapy.Field()
    Rating_count = scrapy.Field()
    Sponsered= scrapy.Field()
    Price = scrapy.Field()
    Sale_price = scrapy.Field()
    Express = scrapy.Field()
    #Rank = scrapy.Field()
    Link = scrapy.Field()
    Get_It_BY = scrapy.Field()
    Date = scrapy.Field()
