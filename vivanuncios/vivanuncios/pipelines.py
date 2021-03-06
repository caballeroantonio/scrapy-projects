# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv

class VivanunciosPipeline(object):
    def __init__(self):
        self.files = {}
        
    @classmethod
    def from_crawler(cls, crawler):
    	pipeline = cls()
    	crawler.signals.connect(pipeline.spider_opened,signals.spider_opened)
    	crawler.signals.connect(pipeline.spider_closed,signals.spider_closed)
    	return pipeline

    def spider_opened(self,spider):
    	file = open('%s_items.csv' % spider.name, 'w+b')
    	self.files[spider] = file
    	self.exporter = CsvItemExporter(file)
    	self.exporter.fields_to_export = [ 
                                            'idPropiedad',
                                            'category_id',
                                            'agent_id',
                                            'user_id', 
                                            'type_popiedad',
                                            'title',
                                            'slug',
                                            'body',
                                            'image_name',
                                            'image_ext',
                                            'meta_keywords',
                                            'meta_desc',
                                            'status',
                                            'create_date',
                                            'updated_at',
                                            'address',
                                            'city',
                                            'state',
                                            'zip_propiedad',
                                            'country',
                                            'latitude',
                                            'longitude',
                                            'price',
                                            'beds',
                                            'services',
                                            'characteristics',
                                            'bath',
                                            'year',
                                            'features',
                                            'is_delete',
                                            'featured',
                                            'size',
                                            'related',
                                            'disponible',
                                            'tipoLetra',
                                            'tipoPublicado',
                                            'url_pagina',
                                            'url_vendedor',
                                            'nombre_vendedor',
                                            'id_anuncio',
                                            'leyenda',
                                            'sitio'
                                            ]
    	self.exporter.start_exporting()

    def spider_closed(self,spider):
    	self.exporter.finish_exporting()
    	file = self.file.pop(spider)
    	file.close()

    def process_item(self, item, spider):
        # build your row to export, then export the row
        self.exporter.export_item(item)
        return item
