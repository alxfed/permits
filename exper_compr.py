# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
from numpy import nan


def main():
    input_file_path = '/media/alxfed/toca/presentation/gen_contractors_new_permits.csv'
    reference_file_path = '/media/alxfed/toca/presentation/unique_gen_contractors.csv'
    input_columns = ['general_contractor', 'id', 'permit_', 'permit_type', 'application_start_date', 'issue_date',
                'street_number', 'street_direction', 'street_name', 'suffix',
                'work_description',
                'contact_1_type', 'contact_1_name', 'contact_1_city', 'contact_1_state', 'contact_1_zipcode',
                'reported_cost',
                'contact_2_type', 'contact_2_name', 'contact_2_city', 'contact_2_state', 'contact_2_zipcode',
                'contact_3_type', 'contact_3_name', 'contact_3_city', 'contact_3_state', 'contact_3_zipcode',
                'contact_4_type', 'contact_4_name', 'contact_4_city', 'contact_4_state', 'contact_4_zipcode',
                'contact_5_type', 'contact_5_name', 'contact_5_city', 'contact_5_state', 'contact_5_zipcode',
                'contact_6_type', 'contact_6_name', 'contact_6_city', 'contact_6_state', 'contact_6_zipcode',
                'contact_7_type', 'contact_7_name', 'contact_7_city', 'contact_7_state', 'contact_7_zipcode',
                'contact_8_type', 'contact_8_name', 'contact_8_city', 'contact_8_state', 'contact_8_zipcode',
                'contact_9_type', 'contact_9_name', 'contact_9_city', 'contact_9_state', 'contact_9_zipcode',
                'contact_10_type', 'contact_10_name', 'contact_10_city', 'contact_10_state', 'contact_10_zipcode',
                'contact_11_type', 'contact_11_name', 'contact_11_city', 'contact_11_state', 'contact_11_zipcode',
                'contact_12_type', 'contact_12_name', 'contact_12_city', 'contact_12_state', 'contact_12_zipcode',
                'contact_13_type', 'contact_13_name', 'contact_13_city', 'contact_13_state', 'contact_13_zipcode',
                'contact_14_type', 'contact_14_name', 'contact_14_city', 'contact_14_state', 'contact_14_zipcode']
    origin      = pd.read_csv(input_file_path)
    reference   = pd.read_csv(reference_file_path)

    big_permits = origin[(origin['general_contractor'] != nan) &
                         (origin['reported_cost'] > 100000) &
                         ((origin['permit_type'] == 'PERMIT - NEW CONSTRUCTION') |
                          (origin['permit_type'] == 'PERMIT - RENOVATION/ALTERATION')
                          )]

    grouped = origin['reported_cost'].groupby(origin['general_contractor']).sum()
    print(grouped)
    return


if __name__ == '__main__':
    main()
    print('main - done')