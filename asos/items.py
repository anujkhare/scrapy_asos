# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AsosItem(scrapy.Item):
    name = scrapy.Field()
    price_orig = scrapy.Field()
    price_cur = scrapy.Field()
    image_url_small = scrapy.Field()
    image_url_large = scrapy.Field()

   #  def __init__(self):
   #      self['price_orig'] = 0
