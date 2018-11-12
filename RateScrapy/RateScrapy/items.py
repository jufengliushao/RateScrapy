# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class RatescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RateItem(Item):
    money_name = Field()                # 货币名字
    date = Field()                      # 更新时间
    time = Field()                      # time
    currency_buy = Field()              # 现汇的买入价
    currency_sole = Field()             # 现汇卖出价
    cash_buy = Field()                  # 现钞买入价
    cash_sole = Field()                 # 现钞卖出价
