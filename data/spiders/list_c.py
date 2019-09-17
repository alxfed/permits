# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from collections import OrderedDict
import scrapy
from data.items import InspTableLine
from datetime import datetime
import re


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


class InspListCSpider(CSVFeedSpider):
    name = 'insp_list_c'
    allowed_domains = ['webapps1.chicago.gov']
    start_urls = ['file:///home/alxfed/dbase/one_test_new_construction.csv']
    headers = ['ID', 'PERMIT#', 'PERMIT_TYPE', 'REVIEW_TYPE', 'APPLICATION_START_DATE',
               'ISSUE_DATE', 'PROCESSING_TIME', 'STREET_NUMBER', 'STREET DIRECTION',
               'STREET_NAME', 'SUFFIX', 'WORK_DESCRIPTION', 'BUILDING_FEE_PAID',
               'ZONING_FEE_PAID', 'OTHER_FEE_PAID', 'SUBTOTAL_PAID',
               'BUILDING_FEE_UNPAID', 'ZONING_FEE_UNPAID', 'OTHER_FEE_UNPAID',
               'SUBTOTAL_UNPAID', 'BUILDING_FEE_WAIVED', 'ZONING_FEE_WAIVED',
               'OTHER_FEE_WAIVED', 'SUBTOTAL_WAIVED', 'TOTAL_FEE', 'CONTACT_1_TYPE',
               'CONTACT_1_NAME', 'CONTACT_1_CITY', 'CONTACT_1_STATE',
               'CONTACT_1_ZIPCODE', 'CONTACT_2_TYPE', 'CONTACT_2_NAME',
               'CONTACT_2_CITY', 'CONTACT_2_STATE', 'CONTACT_2_ZIPCODE',
               'CONTACT_3_TYPE', 'CONTACT_3_NAME', 'CONTACT_3_CITY',
               'CONTACT_3_STATE', 'CONTACT_3_ZIPCODE', 'CONTACT_4_TYPE',
               'CONTACT_4_NAME', 'CONTACT_4_CITY', 'CONTACT_4_STATE',
               'CONTACT_4_ZIPCODE', 'CONTACT_5_TYPE', 'CONTACT_5_NAME',
               'CONTACT_5_CITY', 'CONTACT_5_STATE', 'CONTACT_5_ZIPCODE',
               'CONTACT_6_TYPE', 'CONTACT_6_NAME', 'CONTACT_6_CITY',
               'CONTACT_6_STATE', 'CONTACT_6_ZIPCODE', 'CONTACT_7_TYPE',
               'CONTACT_7_NAME', 'CONTACT_7_CITY', 'CONTACT_7_STATE',
               'CONTACT_7_ZIPCODE', 'CONTACT_8_TYPE', 'CONTACT_8_NAME',
               'CONTACT_8_CITY', 'CONTACT_8_STATE', 'CONTACT_8_ZIPCODE',
               'CONTACT_9_TYPE', 'CONTACT_9_NAME', 'CONTACT_9_CITY',
               'CONTACT_9_STATE', 'CONTACT_9_ZIPCODE', 'CONTACT_10_TYPE',
               'CONTACT_10_NAME', 'CONTACT_10_CITY', 'CONTACT_10_STATE',
               'CONTACT_10_ZIPCODE', 'CONTACT_11_TYPE', 'CONTACT_11_NAME',
               'CONTACT_11_CITY', 'CONTACT_11_STATE', 'CONTACT_11_ZIPCODE',
               'CONTACT_12_TYPE', 'CONTACT_12_NAME', 'CONTACT_12_CITY',
               'CONTACT_12_STATE', 'CONTACT_12_ZIPCODE', 'CONTACT_13_TYPE',
               'CONTACT_13_NAME', 'CONTACT_13_CITY', 'CONTACT_13_STATE',
               'CONTACT_13_ZIPCODE', 'CONTACT_14_TYPE', 'CONTACT_14_NAME',
               'CONTACT_14_CITY', 'CONTACT_14_STATE', 'CONTACT_14_ZIPCODE',
               'CONTACT_15_TYPE', 'CONTACT_15_NAME', 'CONTACT_15_CITY',
               'CONTACT_15_STATE', 'CONTACT_15_ZIPCODE', 'REPORTED_COST',
               'PIN1', 'PIN2', 'PIN3', 'PIN4', 'PIN5', 'PIN6', 'PIN7', 'PIN8',
               'PIN9', 'PIN10', 'COMMUNITY_AREA', 'CENSUS_TRACT', 'WARD',
               'XCOORDINATE', 'YCOORDINATE', 'LATITUDE', 'LONGITUDE',
               'LOCATION', 'Boundaries - ZIP Codes', 'Community Areas',
               'Zip Codes', 'Census Tracts', 'Wards', ':@computed_region_awaf_s7ux']
    INSPECTIONS_URL = 'https://webapps1.chicago.gov/buildingrecords/doSearch'
    VALIDATE_URL = 'https://webapps1.chicago.gov/buildingrecords/validateaddress'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        header_start = self.headers[0]
        if row[header_start].startswith(header_start):
            yield None
        else:
            tup = (row['STREET_NUMBER'], row['STREET DIRECTION'],
                   row['STREET_NAME'], row['SUFFIX'])
            address = " ".join(tup)
            the_kwargs = {'permit_n': row['PERMIT#'],
                          'full_address': address}
            yield scrapy.Request(url=self.INSPECTIONS_URL,
                                 dont_filter=True,
                                 callback=self.parse_table,
                                 cb_kwargs=the_kwargs)

    def parse_table(self, response, **kwargs):
        INSP_ROWS_XPATH = '//*[@id="resultstable_inspections"]/tbody/tr'
        permit = kwargs['permit_n']
        address = kwargs['full_address']
        # minify html
        response = response.replace(body=re.sub('>\s*<', '><',
                                                response.body.replace('\n', ''),
                                                0, re.M))
        # minify html
        if response.url == self.INSPECTIONS_URL:
            # columns: INSP #, INSPECTION DATE, STATUS, TYPE DESCRIPTION
            permits_table_line = dict()
            permits_table_line.update({'permit_n': permit, 'full_address': address})
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
            else:
                insp_list.update(dict())
            permits_table_line.update(insp_list)
            yield permits_table_line
        elif response.url == self.VALIDATE_URL:
            if not_found(response):
                permits_table_line = dict()
                permits_table_line.update({'permit_n': permit, 'full_address': address})
                insp_list = OrderedDict(dict())
                permits_table_line.update(insp_list)
                yield permits_table_line
            else:
                yield None
        else:
            self.logger('Something returned, but I dont know what it is')
            yield None

