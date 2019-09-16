# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from datetime import datetime
from data.items import InspTableLine
from collections import OrderedDict


def agreement_failed(response):
    NO_AGREEMENT_XPATH = '//*[@id="agreement.errors"]/text()'
    no_agreement = response.xpath(NO_AGREEMENT_XPATH).get()
    if no_agreement:
        if no_agreement.startswith('Please agree to the term of the site to confinue.'):
            return True
        else:
            return True
    else:
        return False


def not_found(response):
    # //*[@id="search"]/div[2]/p
    NO_MATCH_XPATH = '//*[@id="search"]/div[2]/p/text()'
    no_address_found = response.xpath(NO_MATCH_XPATH).get()
    if no_address_found:
        if no_address_found.startswith('The address match was not found.'):
            return True
        else:
            return True
    else:
        return False


class InspectionsListSpider(scrapy.Spider):
    name = 'insp_list_a'
    start_urls = ['https://webapps1.chicago.gov/buildingrecords/home']
    DB_PATH = '/home/alxfed/dbase/fifthbase.sqlite'
    conn = sqlite3.connect(DB_PATH)  # , isolation_level=None) for working without commit
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    curs.execute('SELECT "PERMIT#", "STREET_NUMBER", "STREET DIRECTION", "STREET_NAME", "SUFFIX"  FROM permits')
    permits_list = []
    for row in curs.fetchall():
        permits_list.append({'permit_n': row['PERMIT#'],
                             'street_n': row["STREET_NUMBER"],
                             'street_dir': row["STREET DIRECTION"],
                             'street_name': row["STREET_NAME"],
                             'suffix': row["SUFFIX"]})
    conn.close()

    def parse(self, response):
        if agreement_failed(response):
            self.logger.error("agreement failed!")
            return
        for permit in self.permits_list:
            tup = (permit['street_n'], permit['street_dir'],
                   permit['street_name'], permit['suffix'])
            address = " ".join(tup)
            kwargs = {'permit_n': permit['permit_n'],
                      'full_address': address}
            yield scrapy.FormRequest.from_response(
                response,
                formid='search',
                formdata = {"fullAddress": address,  # 1940 N WHIPPLE ST
                            "submit": "submit"},
                callback = self.after_search, cb_kwargs=kwargs)

    def after_search(self, response, **kwargs):
        INSP_ROWS_XPATH = '//*[@id="resultstable_inspections"]/tbody/tr'
        perm = kwargs['permit_n']
        address = kwargs['full_address']
        if not_found(response):
            yield None
        else:
            # columns: INSP #, INSPECTION DATE, STATUS, TYPE DESCRIPTION
            permits_table_line = dict()
            permits_table_line.update({'permit_n': perm, 'full_address': address})
            insp_list = OrderedDict()
            insp_table = response.xpath(INSP_ROWS_XPATH)
            if insp_table:
                for line in insp_table:
                    table_line = InspTableLine()
                    table_line['insp_n'] = line.xpath('td[1]/text()').get()
                    insp_date = datetime.strptime(line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                    table_line['insp_date'] = insp_date.strftime('%Y-%m-%d')
                    table_line['status'] = line.xpath('td[3]/text()').get()
                    table_line['type_desc'] = line.xpath('td[4]/text()').get()
                    insp_list.update(table_line)
                permits_table_line.update(insp_list)
            yield permits_table_line
