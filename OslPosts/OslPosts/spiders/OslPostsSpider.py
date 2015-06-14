# -*- coding: utf-8 -*-
import scrapy


class OslpostsspiderSpider(scrapy.Spider):
    name = "OslPostsSpider"
    allowed_domains = ["osl.ugr.es"]
    start_urls = (
        'http://www.osl.ugr.es/',
    )

    def parse(self, response):
        pass
