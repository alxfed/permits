# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from collections import OrderedDict
import scrapy


class InspListCSpider(CSVFeedSpider):
    name = 'insp_list_c'
    allowed_domains = ['webapps1.chicago.gov']
    start_urls = ['file:///home/alxfed/dbase/test_new_construction.csv']
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

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        header_start = self.headers[0]
        if row[header_start].startswith(header_start):
            yield None
        else:
            yield scrapy.Request('https://webapps1.chicago.gov/buildingrecords/home')
