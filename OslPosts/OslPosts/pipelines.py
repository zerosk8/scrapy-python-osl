# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

class OslpostsPipeline(object):
    def __init__(self):
        self.nombre_fichero = [
                        'items_tags.xml',
                        'items_no_tags.xml'
                        ]
        self.fichero = {}
        self.exporter = {}
    
    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline
    
    def spider_opened(self, spider):
        self.fichero['tags'] = open(self.nombre_fichero[0], 'w+b')
        self.fichero['no_tags'] = open(self.nombre_fichero[1], 'w+b')
        
        self.exporter['tags'] = XmlItemExporter(self.fichero['tags'])
        self.exporter['no_tags'] = XmlItemExporter(self.fichero['no_tags'])
        
        self.exporter['tags'].start_exporting()
        self.exporter['no_tags'].start_exporting()
    
    def spider_closed(self, spider):
        self.exporter['tags'].finish_exporting()
        self.exporter['no_tags'].finish_exporting()
        
        for k, v in self.fichero.items():
            v.close()
    
    def process_item(self, item, spider):
        # Eliminacion de etiquetas de "HTML" en el contenido del post
        item['contenido'] = re.sub("<[^>]+>", "", item['contenido'])
        
        if item['etiquetas']:
            self.exporter['tags'].export_item(item)
        else:
            self.exporter['no_tags'].export_item(item)
            
        return item
