# -*- coding: utf-8 -*-
"""...
"""
from numpy import nan
import numpy as np
from datetime import datetime
import pandas as pd


def dateparse(x):
    if x is nan:
        return datetime(2018, 12, 8, 0, 0)
    else:
        return pd.datetime.strptime(x, '%Y-%m-%d') #  %H:%M:%S.%f if there are hours, minutes, seconts and milliseconds


def main():
    unique_gen_contractors = set()
    output_list = list()
    input_file = '/media/alxfed/toca/presentation/all_new_permits.csv'
    output_file = '/media/alxfed/toca/presentation/unique_gen_contractors.csv'
    col_type = {'id': np.int, 'permit_': np.int, 'permit_type': object, 'review_type': object,
                'application_start_date': object, 'issue_date': object, 'processing_time': object,
                'street_number': object, 'street_direction': object, 'street_name': object, 'suffix': object,
                'work_description': object,
                'building_fee_paid': object, 'zoning_fee_paid': object, 'other_fee_paid': object,
                'subtotal_paid': object, 'building_fee_unpaid': object, 'zoning_fee_unpaid': object,
                'other_fee_unpaid': object, 'subtotal_unpaid': object, 'building_fee_waived': object,
                'zoning_fee_waived': object, 'other_fee_waived': object, 'subtotal_waived': object,
                'total_fee': object,
                'contact_1_type': object, 'contact_1_name': object, 'contact_1_city': object,
                'contact_1_state': object, 'contact_1_zipcode': object,
                'reported_cost': np.float64, 'pin1': object,
                'community_area': object, 'census_tract': object, 'ward': object,
                'xcoordinate': object, 'ycoordinate': object, 'latitude': object, 'longitude': object,
                'location': object,
                'contact_2_type': object, 'contact_2_name': object, 'contact_2_city': object,
                'contact_2_state': object, 'contact_2_zipcode': object,
                'contact_3_type': object, 'contact_3_name': object, 'contact_3_city': object,
                'contact_3_state': object, 'contact_3_zipcode': object,
                'pin2': object, 'pin3': object, 'pin4': object,
                'contact_4_type': object, 'contact_4_name': object, 'contact_4_city': object,
                'contact_4_state': object, 'contact_4_zipcode': object,
                'contact_5_type': object, 'contact_5_name': object, 'contact_5_city': object,
                'contact_5_state': object, 'contact_5_zipcode': object,
                'contact_6_type': object, 'contact_6_name': object, 'contact_6_city': object,
                'contact_6_state': object, 'contact_6_zipcode': object,
                'contact_7_type': object, 'contact_7_name': object, 'contact_7_city': object,
                'contact_7_state': object, 'contact_7_zipcode': object,
                'contact_8_type': object, 'contact_8_name': object, 'contact_8_city': object,
                'contact_8_state': object, 'contact_8_zipcode': object,
                'contact_9_type': object, 'contact_9_name': object, 'contact_9_city': object,
                'contact_9_state': object, 'contact_9_zipcode': object,
                'contact_10_type': object, 'contact_10_name': object, 'contact_10_city': object,
                'contact_10_state': object, 'contact_10_zipcode': object,
                'pin5': object, 'pin6': object, 'pin7': object, 'pin8': object, 'pin9': object, 'pin10': object,
                'contact_11_type': object, 'contact_11_name': object, 'contact_11_city': object,
                'contact_11_state': object, 'contact_11_zipcode': object,
                'contact_12_type': object, 'contact_12_name': object, 'contact_12_city': object,
                'contact_12_state': object, 'contact_12_zipcode': object,
                'contact_13_type': object, 'contact_13_name': object, 'contact_13_city': object,
                'contact_13_state': object, 'contact_13_zipcode': object,
                'contact_14_type': object, 'contact_14_name': object, 'contact_14_city': object,
                'contact_14_state': object, 'contact_14_zipcode': object}
    data = pd.read_csv(input_file,
                       parse_dates=['application_start_date',
                                    'issue_date'],
                       date_parser=dateparse,
                       dtype=col_type)
    for row_n, row in data.iterrows():
        if row['reported_cost'] > 100000:
            for n in range(14):
                contact_type = row[f'contact_{str(n+1)}_type']
                if contact_type == 'CONTRACTOR-GENERAL CONTRACTOR':
                    name = row[f'contact_{str(n+1)}_name']
                    if name not in unique_gen_contractors:
                        unique_gen_contractors.add(name)
                        line = {
                            'name': name,
                            'city': row[f'contact_{str(n+1)}_city'],
                            'state': row[f'contact_{str(n+1)}_state'],
                            'zip': row[f'contact_{str(n+1)}_zipcode'],
                        }
                        output_list.append(line)
                        print(line)

    output = pd.DataFrame(output_list)
    output.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()
    print('main - done')


'''
parse_dates=['application_start_date',
                                     'issue_date'],
                        date_parser=dateparse,
'''