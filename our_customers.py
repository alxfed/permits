# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def is_our_client(row, reference):
    client = ''
    total_revenue = ''
    for indx, co in reference.iterrows():
        if row['general_contractor'] == indx.upper():
            client = 'yes'
            total_revenue = co['Amount in company currency']
    return pd.Series([client, total_revenue])


def main():
    totalput_csv_file_path = '/media/alxfed/toca/presentation/total_pivot_permits.csv'
    pivot_columns =['general_contractor', 'reported_cost']
    pivot_col_types = {'general_contractor': object, 'reported_cost': np.float}

    reference_csv_file_path = '/media/alxfed/toca/presentation/completed_deals.csv'
    ref_columns = ['Associated Company', 'Amount in company currency']
    ref_types = {'Associated Company': object, 'Amount in company currency': np.float}

    clients_reference_file_path = '/media/alxfed/toca/presentation/clients_reference.csv'

    output_file_path = '/media/alxfed/toca/presentation/us_and_total_pivot_permits.csv'

    pivot = pd.read_csv(totalput_csv_file_path, usecols=pivot_columns, dtype=pivot_col_types)
    ref = pd.read_csv(reference_csv_file_path, usecols=ref_columns, dtype=ref_types)
    refer = ref.pivot_table(index=['Associated Company'], values='Amount in company currency', aggfunc=np.sum)

    output = pd.DataFrame()
    output[pivot_columns] = pivot[pivot_columns]
    output[['our_client', 'total_revenue']] = pivot.apply(func=is_our_client, axis=1, reference=refer)
    output.to_csv(output_file_path)
    refer.to_csv(clients_reference_file_path)

    return


if __name__ == '__main__':
    main()
    print('main - done')