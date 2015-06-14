# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OslPost(scrapy.Item):
    nombre = scrapy.Field()
    autor = scrapy.Field()
    contenido = scrapy.Field()
    categorias = scrapy.Field()
    etiquetas = scrapy.Field()
