# -*- coding: utf-8 -*-
import scrapy
import sqlite3


def agreement_failed(response):
    NO_AGREEMENT_XPATH = '//*[@id="agreement.errors"]/text()'
    no_agreement = response.xpath(NO_AGREEMENT_XPATH).get()
    if no_agreement.startswith('Please agree to the term of the site to confinue.'):
        return True
    else:
        return False


def not_found(response):
    # TODO: check if this is a 'not found' page
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
                formdata = {"fullAddress": permit['Address'],
                            "submit": "submit"},
                callback = self.after_search)

    def after_search(self, response):
        if not_found(response):
            yield None
        else:
            # TODO: process the result page
            inspections_list = []
            yield inspections_list
