# -*- coding: utf-8 -*-
"""ingest csv file (even if there are gaps, that's why nan is here)
and format the dates into a unix timestamp like format.
"""
import pandas as pd
from numpy import nan
from datetime import datetime, date, time


def dateparse(x):
    if x is nan:
        return datetime(2018, 12, 8, 0, 0)
    else:
        return pd.datetime.strptime(x, '%m/%d/%Y')


def main():
    input_file_path = '/home/alxfed/Downloads/Building_Permits.csv'
    output_file_path = '/home/alxfed/Downloads/Transformed_Building_Permits.csv'

    start_date = datetime(2018, 12, 8, 0, 0)
    end_date = datetime(2019, 9, 18, 0, 0)

    col_type = {'ID': int, 'PERMIT#': int,
                'PERMIT_TYPE': object, 'REVIEW_TYPE':object,
                'APPLICATION_START_DATE':object, 'ISSUE_DATE':object,
                'PROCESSING_TIME':object,
                'STREET_NUMBER':str, 'STREET DIRECTION':str, 'STREET_NAME':str,
                'SUFFIX':str, 'WORK_DESCRIPTION':object,
                'BUILDING_FEE_PAID':float, 'ZONING_FEE_PAID':float, 'OTHER_FEE_PAID':float,
                'SUBTOTAL_PAID':float, 'BUILDING_FEE_UNPAID':float, 'ZONING_FEE_UNPAID':float,
                'OTHER_FEE_UNPAID':float, 'SUBTOTAL_UNPAID':float, 'BUILDING_FEE_WAIVED':float,
                'ZONING_FEE_WAIVED':float, 'OTHER_FEE_WAIVED':float, 'SUBTOTAL_WAIVED':float,
                'TOTAL_FEE':float,
                'CONTACT_1_TYPE':object, 'CONTACT_1_NAME': object, 'CONTACT_1_CITY': object, 'CONTACT_1_STATE': object, 'CONTACT_1_ZIPCODE': object,
                'CONTACT_2_TYPE': object, 'CONTACT_2_NAME': object, 'CONTACT_2_CITY': object, 'CONTACT_2_STATE': object, 'CONTACT_2_ZIPCODE': object,
                'CONTACT_3_TYPE': object, 'CONTACT_3_NAME': object, 'CONTACT_3_CITY': object, 'CONTACT_3_STATE': object, 'CONTACT_3_ZIPCODE': object,
                'CONTACT_4_TYPE': object, 'CONTACT_4_NAME': object, 'CONTACT_4_CITY': object, 'CONTACT_4_STATE': object, 'CONTACT_4_ZIPCODE': object,
                'CONTACT_5_TYPE': object, 'CONTACT_5_NAME': object, 'CONTACT_5_CITY': object, 'CONTACT_5_STATE': object, 'CONTACT_5_ZIPCODE': object,
                'CONTACT_6_TYPE': object, 'CONTACT_6_NAME': object, 'CONTACT_6_CITY': object, 'CONTACT_6_STATE': object, 'CONTACT_6_ZIPCODE': object,
                'CONTACT_7_TYPE': object, 'CONTACT_7_NAME': object, 'CONTACT_7_CITY': object, 'CONTACT_7_STATE': object, 'CONTACT_7_ZIPCODE': object,
                'CONTACT_8_TYPE': object, 'CONTACT_8_NAME': object, 'CONTACT_8_CITY': object, 'CONTACT_8_STATE': object, 'CONTACT_8_ZIPCODE': object,
                'CONTACT_9_TYPE': object, 'CONTACT_9_NAME': object, 'CONTACT_9_CITY': object, 'CONTACT_9_STATE': object, 'CONTACT_9_ZIPCODE': object,
                'CONTACT_10_TYPE': object, 'CONTACT_10_NAME': object, 'CONTACT_10_CITY': object, 'CONTACT_10_STATE': object, 'CONTACT_10_ZIPCODE': object,
                'CONTACT_11_TYPE': object, 'CONTACT_11_NAME': object, 'CONTACT_11_CITY': object, 'CONTACT_11_STATE': object, 'CONTACT_11_ZIPCODE': object,
                'CONTACT_12_TYPE': object, 'CONTACT_12_NAME': object, 'CONTACT_12_CITY': object, 'CONTACT_12_STATE': object, 'CONTACT_12_ZIPCODE': object,
                'CONTACT_13_TYPE': object, 'CONTACT_13_NAME': object, 'CONTACT_13_CITY': object, 'CONTACT_13_STATE': object, 'CONTACT_13_ZIPCODE': object,
                'CONTACT_14_TYPE': object, 'CONTACT_14_NAME': object, 'CONTACT_14_CITY': object, 'CONTACT_14_STATE': object, 'CONTACT_14_ZIPCODE': object,
                'CONTACT_15_TYPE': object, 'CONTACT_15_NAME': object, 'CONTACT_15_CITY': object, 'CONTACT_15_STATE': object, 'CONTACT_15_ZIPCODE': object,
                'REPORTED_COST':float,
                'PIN1':str, 'PIN2':str, 'PIN3':str, 'PIN4':str, 'PIN5':str, 'PIN6':str, 'PIN7':str, 'PIN8':str, 'PIN9':str, 'PIN10':str,
                'COMMUNITY_AREA': int, 'CENSUS_TRACT': int, 'WARD': int,
                'XCOORDINATE':float, 'YCOORDINATE':float, 'LATITUDE': float, 'LONGITUDE': float,
                'LOCATION': object, 'Boundaries - ZIP Codes': int, 'Community Areas': int, 'Zip Codes': int, 'Census Tracts': int, 'Wards': int,
                ':@computed_region_awaf_s7ux': object}

    rfile = pd.read_csv(input_file_path,
                           parse_dates=['APPLICATION_START_DATE',
                                        'ISSUE_DATE'],
                           date_parser=dateparse,
                           dtype=object)

    rfile['REPORTED_COST'] = pd.to_numeric(rfile['REPORTED_COST'])
    new_permits = rfile[rfile['ISSUE_DATE'] > start_date]
    new_large_permits = new_permits[new_permits['REPORTED_COST'] > 50000]
    new_renovations = new_large_permits[new_large_permits['PERMIT_TYPE'] == 'PERMIT - RENOVATION/ALTERATION']
    new_new_constructions = new_large_permits[new_large_permits['PERMIT_TYPE'] == 'PERMIT - NEW CONSTRUCTION']

    new_renovations.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')