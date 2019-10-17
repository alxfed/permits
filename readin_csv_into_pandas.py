# -*- coding: utf-8 -*-
"""...
"""
from numpy import nan
from datetime import datetime
import pandas as pd


def dateparse(x):
    if x is nan:
        return datetime(2018, 12, 8, 0, 0)
    else:
        return pd.datetime.strptime(x, '%Y-%m-%d') #  %H:%M:%S.%f if there are hours, minutes, seconts and milliseconds


def main():
    input_file = '/media/alxfed/toca/presentation/all_new_permits.csv'
    columns = ['id', 'permit_', 'permit_type', 'review_type', 'application_start_date',
               'issue_date', 'processing_time', 'street_number', 'street_direction',
               'street_name', 'suffix', 'work_description', 'building_fee_paid',
               'zoning_fee_paid', 'other_fee_paid', 'subtotal_paid', 'building_fee_unpaid',
               'zoning_fee_unpaid', 'other_fee_unpaid', 'subtotal_unpaid',
               'building_fee_waived', 'zoning_fee_waived', 'other_fee_waived',
               'subtotal_waived', 'total_fee',
               'contact_1_type', 'contact_1_name', 'contact_1_city', 'contact_1_state', 'contact_1_zipcode',
               'reported_cost', 'pin1', 'community_area', 'census_tract', 'ward', 'xcoordinate',
               'ycoordinate', 'latitude', 'longitude', 'location',
               'contact_2_type', 'contact_2_name', 'contact_2_city', 'contact_2_state', 'contact_2_zipcode',
               'contact_3_type', 'contact_3_name', 'contact_3_city', 'contact_3_state', 'contact_3_zipcode',
               'pin2', 'pin3', 'pin4',
               'contact_4_type', 'contact_4_name', 'contact_4_city', 'contact_4_state', 'contact_4_zipcode',
               'contact_5_type', 'contact_5_name', 'contact_5_city', 'contact_5_state', 'contact_5_zipcode',
               'contact_6_type', 'contact_6_name', 'contact_6_city', 'contact_6_state', 'contact_6_zipcode',
               'contact_7_type', 'contact_7_name', 'contact_7_city', 'contact_7_state', 'contact_7_zipcode',
               'contact_8_type', 'contact_8_name', 'contact_8_city', 'contact_8_state', 'contact_8_zipcode',
               'contact_9_type', 'contact_9_name', 'contact_9_city', 'contact_9_state', 'contact_9_zipcode',
               'contact_10_type', 'contact_10_name', 'contact_10_city', 'contact_10_state', 'contact_10_zipcode',
               'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10',
               'contact_11_type', 'contact_11_name', 'contact_11_city', 'contact_11_state', 'contact_11_zipcode',
               'contact_12_type', 'contact_12_name', 'contact_12_city', 'contact_12_state', 'contact_12_zipcode',
               'contact_13_type', 'contact_13_name', 'contact_13_city', 'contact_13_state', 'contact_13_zipcode',
               'contact_14_type', 'contact_14_name', 'contact_14_city', 'contact_14_state', 'contact_14_zipcode']
    data = pd.read_csv(input_file,
                        parse_dates=['application_start_date',
                                     'issue_date'],
                        date_parser=dateparse,
                        dtype=object)
    return


if __name__ == '__main__':
    main()
    print('main - done')