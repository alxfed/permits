# -*- coding: utf-8 -*-
"""Add contractor columns to new format of permits data
"""
import pandas as pd
import numpy as np


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
    return pd.Series([general_contractor, month])


def main():
    origin_file_path = '/media/alxfed/toca/presentation/gen_contractors_new_permits.csv'
    output_file_path = '/media/alxfed/toca/presentation/pivot_new_permits.csv'
    output_excel_file_path = '/media/alxfed/toca/presentation/pivot_new_permits.xlsx'
    totalput_excel_file_path = '/media/alxfed/toca/presentation/total_pivot_permits.xlsx'
    totalput_csv_file_path = '/media/alxfed/toca/presentation/total_pivot_permits.csv'

    useful_columns = ['general_contractor', 'reported_cost', 'permit_', 'permit_type', 'issue_date', 'month',
                      'street_number', 'street_direction', 'street_name', 'suffix', 'work_description']

    column_types = {'reported_cost': np.float, 'permit_': np.int, 'permit_type': object,
                    'issue_date': object}

    origin = pd.read_csv(origin_file_path, usecols=useful_columns, parse_dates=['issue_date'], dtype=column_types)

    output = pd.DataFrame()
    output = origin.sort_values(by=['general_contractor', 'month'])
    totals = origin.pivot_table(index=['general_contractor'], values='reported_cost', aggfunc=np.sum)
    totals.to_excel(totalput_excel_file_path, sheet_name='Sheet 0', float_format="%.2f",
                   merge_cells=True)
    totals.to_csv(totalput_csv_file_path)
    pivot = origin.pivot_table(index=['general_contractor', 'month'], values='reported_cost',
                               aggfunc= [np.sum, np.mean])
    pivot.to_excel(output_excel_file_path, sheet_name='Sheet 0', float_format="%.2f",
                   merge_cells=True)
    output.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')
