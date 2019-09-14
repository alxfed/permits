# -*- coding: utf-8 -*-
import scrapy
from os import environ
from sodapy import Socrata
# https://data.cityofchicago.org/resource/ydr8-5enu.json


class SocrataSpider(scrapy.Spider):
    name = 'socrata'
    allowed_domains = ['data.cityofchicago.org']
    start_urls = ['http://data.cityofchicago.org/']
    api_key = environ.get('API_KEY')
    dataset_identifier = 'ydr8-5enu'

    def parse(self, response):
        pass
