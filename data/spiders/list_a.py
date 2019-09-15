# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from datetime import datetime
from data.items import InspTableLine
from collections import OrderedDict


def agreement_failed(response):
    NO_AGREEMENT_XPATH = '//*[@id="agreement.errors"]/text()'
    no_agreement = response.xpath(NO_AGREEMENT_XPATH).get()
    if no_agreement.startswith('Please agree to the term of the site to confinue.'):
        return True
    else:
        return False


def not_found(response):
    # //*[@id="search"]/div[2]/p
    NO_MATCH_XPATH = '//*[@id="search"]/div[2]/p/text()'
    no_address_found = response.xpath(NO_MATCH_XPATH).get()
    if no_address_found.startswith('The address match was not found.'):
        return True
    else:
        return False


class InspectionsListSpider(scrapy.Spider):
    name = 'insp_list_a'
    start_urls = ['https://webapps1.chicago.gov/buildingrecords/home']
    DB_PATH = '/media/alxfed/toca/dbase/fifthbase.sqlite'
    conn = sqlite3.connect(DB_PATH)  # , isolation_level=None) for working without commit
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formid='agreement',
            formdata = {"agreement": "Y",
                        "submit": "submit"},
            callback = self.after_agreement
        )

    def after_agreement(self, response):
        if agreement_failed(response):
            self.logger.error("agreement failed!")
            return
        else:
            self.curs.execute("SELECT Address From permits")
            permits_list = self.curs.fetchall()
        for permit in permits_list:
            yield scrapy.FormRequest.from_response(
                response,
                formid='search',
                formdata = {"fullAddress": permit['Address'],  # 1940 N WHIPPLE ST
                            "submit": "submit"},
                callback = self.after_search)

    def after_search(self, response):
        INSP_ROWS_XPATH = '//*[@id="resultstable_inspections"]/tbody/tr'
        if not_found(response):
            yield None
        else:
            # columns: INSP #, INSPECTION DATE, STATUS, TYPE DESCRIPTION
            insp_list = OrderedDict()
            insp_table = response.xpath(INSP_ROWS_XPATH)
            for line in insp_table:
                table_line = InspTableLine()
                table_line['insp_n'] = line.xpath('td[1]/text()').get()
                insp_date = datetime.strptime(line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                table_line['insp_date'] = insp_date.strftime('%Y-%m-%d')
                table_line['status'] = line.xpath('td[3]/text()').get()
                table_line['type_desc'] = line.xpath('td[4]/text()').get()
                insp_list.update(table_line)
            yield insp_list
