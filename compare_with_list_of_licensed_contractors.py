# -*- coding: utf-8 -*-
"""https://www.chicago.gov/city/en/depts/bldgs/provdrs/gen_contract.html
"""
import pandas as pd
from datetime import datetime
import numpy as np
from numpy import nan


def dateparse(x):
    if x is nan:
        return # datetime(2018, 12, 8, 0, 0)
    else:
        return pd.datetime.strptime(x, '%m/%d/%y') #  %H:%M:%S.%f if there are hours, minutes, seconts and milliseconds


def compare_with_licenses(row, reference):
    general_contractor = row['general_contractor']
    [one, two, three] = general_contractor.split(sep=' ', maxsplit=3)
    for index, name in reference.iterrows():
        company_name = name['company_name']
        [one_r, two_r, three_r] = company_name.split(sep=' ', maxsplit=3)
        if one_r == one.upper():
            if two_r == two.upper():
                if three_r == three.upper():
                    break
        else:
            pass
    return general_contractor


def main():
    # active General Contractors are on https://webapps1.chicago.gov/activegcWeb/
    origin_file_path = '/media/alxfed/toca/presentation/gen_contractors_new_permits.csv'
    output_file_path = '/home/alxfed/archive/verified_gen_contractors_new_permits.csv'
    output_excel_file_path = '/media/alxfed/toca/presentation/verified_gen_contractors_new_permits.xlsx'

    useful_columns = ['general_contractor', 'reported_cost', 'permit_', 'permit_type', 'issue_date', 'month',
                      'street_number', 'street_direction', 'street_name', 'suffix', 'work_description']

    column_types = {'reported_cost': np.float, 'permit_': np.int, 'permit_type': object,
                    'issue_date': object}

    origin = pd.read_csv(origin_file_path, usecols=useful_columns,
                                    parse_dates=['issue_date'],
                                    dtype=column_types)

    gen_cont_file_path = '/home/alxfed/archive/licensed_general_contractors.csv'

    gen_contractors = pd.read_csv(gen_cont_file_path,
                                    parse_dates=['license_expr',
                                                 'primary_insurance_expr',
                                                 'secondary_insurance_expr'],
                                    date_parser=dateparse,
                                    dtype=object)

    output = pd.DataFrame()
    output['general_contractor'] = origin.apply(compare_with_licenses, axis=1, reference=gen_contractors)

    return


if __name__ == '__main__':
    main()
    print('main - done')