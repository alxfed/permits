# -*- coding: utf-8 -*-
"""Add contractor columns to new format of permits data
"""
import pandas as pd
from datetime import datetime


def additional_column(row):
    month = row['issue_date'].strftime("%b") # str
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
    return general_contractor, month


def main():
    useful_columns = ['reported_cost', 'permit_', 'permit_type', 'issue_date',
                      'street_number', 'street_direction', 'street_name', 'suffix',
                      'work_description']

    origin_file_path = '/media/alxfed/toca/presentation/all_new_permits.csv'
    output_file_path = '/media/alxfed/toca/presentation/gen_contractors_new_permits.csv'

    origin = pd.read_csv(origin_file_path, parse_dates=['application_start_date',
                                     'issue_date'])
    origin = origin[(origin['reported_cost'] > 100000) &
                    ((origin['permit_type'] == 'PERMIT - NEW CONSTRUCTION') |
                     (origin['permit_type'] == 'PERMIT - RENOVATION/ALTERATION'))]

    output = pd.DataFrame()

    output[['general_contractor', 'month']] = origin.apply(additional_column, axis=1)
    output[useful_columns] = origin[useful_columns]
    output = output[output['general_contractor'] != '']
    output.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')
