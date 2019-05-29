# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutulaItem(scrapy.Item):
    # define the fields for your item here like:
    image_list = scrapy.Field()
    # image_path = scrapy.Field()  # 图片本地存储路径(相对路径)
