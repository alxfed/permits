# -*- coding: utf-8 -*-
import scrapy


class SocrataSpider(scrapy.Spider):
    name = 'socrata'
    allowed_domains = ['cityofchicago.gov']
    start_urls = ['http://cityofchicago.gov/']

    def parse(self, response):
        pass
