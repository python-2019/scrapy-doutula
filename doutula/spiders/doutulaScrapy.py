#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

# 这里是正确的 应该以spider上级目录为根目录
from doutula.items import DoutulaItem


class doutulaScrapy(scrapy.Spider):
    name = 'doutula'
    allowed_domains = ["www.doutula.com"]
    host = "http://www.doutula.com"
    start_urls = (
        host + "/photo/list/",
    )

    def parse(self, response):
        item = DoutulaItem()
        item['image_list'] = response.xpath("//a[@class='col-xs-6 col-sm-3']/img[@class='img-responsive lazy image_dta loaded']/@src").extract()
        yield item
        #     翻页
        next_page = response.xpath("//a[contains(text(),'›')]/@href").extract_first()
        if next_page is not None:
            next_page_url = self.host + next_page
            print(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
