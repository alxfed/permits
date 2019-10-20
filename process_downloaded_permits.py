# -*- coding: utf-8 -*-
"""Add contractor columns to new format of permits data
"""
import pandas as pd
import numpy as np
from datetime import datetime


def additional_column(row):
    month = row['issue_date'].strftime("%-m") # str
    general_contractor = ''
    for n in range(14):
        contact_number = str(n + 1)
        con_type_key = f'contact_{contact_number}_type'
        if con_type_key in row.keys():
            contact_type = row[con_type_key]
            if contact_type == 'CONTRACTOR-GENERAL CONTRACTOR':
                general_contractor = row[f'contact_{contact_number}_name']
        else:
            break
    return pd.Series([general_contractor, month])


def main():
    use_columns = ['id', 'permit_', 'permit_type', 'issue_date',
                   'street_number', 'street_direction', 'street_name', 'suffix',
                   'work_description', 'reported_cost',
                      'contact_1_type', 'contact_1_name', 'contact_1_city', 'contact_1_state', 'contact_1_zipcode',
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

    column_types = {'id': np.int, 'permit_': np.int,
                    'permit_type': object,
                    'issue_date': object, 'reported_cost': np.float}

    origin_file_path = '/media/alxfed/toca/presentation/all_new_permits.csv'
    output_file_path = '/media/alxfed/toca/presentation/gen_contractors_new_permits.csv'

    origin = pd.read_csv(origin_file_path, usecols=use_columns,
                         parse_dates=['issue_date'], dtype=column_types)
    origin = origin[(origin['reported_cost'] > 100000) &
                    ((origin['permit_type'] == 'PERMIT - NEW CONSTRUCTION') |
                     (origin['permit_type'] == 'PERMIT - RENOVATION/ALTERATION'))]

    output = pd.DataFrame()

    output[['general_contractor', 'month']] = origin.apply(additional_column, axis=1)
    output[use_columns] = origin[use_columns]
    # filter out the rows without a company
    output = output[output['general_contractor'] != '']
    output.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')
