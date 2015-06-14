# -*- coding: utf-8 -*-
import scrapy


class OslUgrSpider(scrapy.Spider):
    name = "osl-ugr"
    allowed_domains = ["osl.ugr.es"]
    start_urls = (
        'http://osl.ugr.es/',
    )

    def parse(self, response):
        pass
