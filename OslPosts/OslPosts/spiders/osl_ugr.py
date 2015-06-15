# -*- coding: utf-8 -*-
import scrapy
from OslPosts.items import OslPost

class OslUgrSpider(scrapy.Spider):
    name = "osl-ugr"
    allowed_domains = ["osl.ugr.es"]
    start_urls = (
        'http://osl.ugr.es/',
    )

    def parse(self, response):
        for url in response.xpath('//h2/a/@href').extract():
            yield scrapy.Request(url, callback = self.parse_item)
    
    def parse_item(self, response):
        post = OslPost()
        
        post['nombre'] = response.xpath('//h1/text()').extract().pop(0)
        post['autor'] = response.xpath('//a[@rel = "author"]/text()').extract().pop(0)
        
        lista = response.xpath('//section[contains(@class, "entry-content")]/*[not(@class="shareinpost")]').extract()
        post['contenido'] = "\n".join(lista)
        
        post['categorias'] = response.xpath('//div[contains(@class, "entry-meta")]/a[contains(@href, "category")]/text()').extract()
        post['etiquetas'] = response.xpath('//div[contains(@class, "entry-meta")]/a[contains(@href, "tag")]/text()').extract()
        
        return post
