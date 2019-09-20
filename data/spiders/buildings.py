# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from collections import OrderedDict
import scrapy
from data.items import InspTableLine, PermTableLine
from datetime import datetime
import re


def not_identified(response):
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


def not_found(response):
    # //*[@id="search"]/div[2]/p
    NO_RESULTS_XPATH = '//*[@id="search"]/div[2]/p/text()'
    no_address_found = response.xpath(NO_RESULTS_XPATH).get()
    if no_address_found:
        if no_address_found.startswith('No results found for this address.'):
            return True
        else:
            return True
    else:
        return False



class InspListCSpider(CSVFeedSpider):
    name = 'buildings'
    allowed_domains = ['webapps1.chicago.gov']
    start_urls = ['file:///home/alxfed/dbase/renovation_alteration.csv']
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
        PERM_ROWS_XPATH = '//*[@id="resultstable_permits"]/tbody/tr'
        INSP_ROWS_XPATH = '//*[@id="resultstable_inspections"]/tbody/tr'
        table_line = OrderedDict()
        perm_list = []
        insp_list = []
        table_line.update({'full_address': kwargs['full_address'],
                           'input_address': kwargs['full_address'],
                           'range_address': '',
                           'perm_table': '',
                           'insp_table': ''})
        if response.url == self.INSPECTIONS_URL and not not_found(response):
            input_address = response.xpath('/html/body/div/div[4]/div[3]/p/text()').get()
            range_address = response.xpath('/html/body/div/div[4]/div[4]/p/text()').get()
            table_line.update({'input_address': input_address,
                               'range_address': range_address})
            perm_table_selector = response.xpath(PERM_ROWS_XPATH)
            # columns: PERMIT #, DATE ISSUED, DESCRIPTION OF WORK
            if perm_table_selector:
                for perm_line in perm_table_selector:
                    perm_table_line = PermTableLine()
                    # //*[@id="resultstable_permits"]/tbody/tr[1]/td[1]
                    perm_table_line['permit_n'] = perm_line.xpath('td[1]/text()').get()
                    perm_date = datetime.strptime(perm_line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                    perm_table_line['perm_date'] = perm_date.strftime('%Y-%m-%d')
                    perm_table_line['work_desc'] = perm_line.xpath('td[3]/text()').get()
                    perm_list.append(perm_table_line)
            else:
                perm_list.append(dict())
            table_line.update({'perm_table': perm_list})
            insp_table_selector = response.xpath(INSP_ROWS_XPATH)
            # columns: INSP #, INSPECTION DATE, STATUS, TYPE DESCRIPTION
            if insp_table_selector:
                for insp_line in insp_table_selector:
                    insp_table_line = InspTableLine()
                    # //*[@id="resultstable_inspections"]/tbody/tr[1]/td[1]/a
                    insp_table_line['insp_n'] = insp_line.xpath('td[1]/a/text()').get()
                    # insp_date = datetime.strptime(insp_line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                    insp_table_line['insp_date'] = insp_line.xpath('td[2]/text()').get() # insp_date.strftime('%Y-%m-%d')
                    # insp_table_line['insp_date'] = insp_line.xpath('td[2]/text()').get()
                    insp_table_line['status'] = insp_line.xpath('td[3]/text()').get()
                    insp_table_line['type_desc'] = insp_line.xpath('td[4]/text()').get()
                    insp_list.append(insp_table_line)
            else:
                insp_list.append(dict())
            table_line.update({'insp_table': insp_list})
            yield table_line
        elif response.url == self.VALIDATE_URL:
            if not_identified(response):
                table_line.update({'input_address': 'Not identified'})
                yield table_line
            else:
                table_line.update({'input_address': 'Not searcheable'})
                yield table_line
        else:
            table_line.update({'input_address': 'Not found'})
            yield table_line

