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
        return pd.datetime.strptime(x, '%m/%d/%Y %H:%M') # :%S.%f if there are seconts and milliseconds


def main():
    input_file_path = '/home/alxfed/archive/Probidder_Sold_Properties_Research_Sheet0_test.csv'
    # renovations_file_path = '/home/alxfed/Downloads/Renovations_Permits.csv'
    # new_constructions_path = '/home/alxfed/Downloads/New_Construction_Permits.csv'

    start_date = datetime(2018, 12, 8, 0, 0)
    end_date = datetime(2019, 9, 18, 0, 0)


    rfile = pd.read_csv(input_file_path,
                        parse_dates=['Probidder Sold Date'],
                        date_parser=dateparse,
                        dtype=object, index_col=False)

    rfile['REPORTED_COST'] = pd.to_numeric(rfile['Probidder Sales Price'], errors='coerce')
    pass
    # new_permits = rfile[rfile['ISSUE_DATE'] > start_date]
    #new_large_permits = new_permits[new_permits['REPORTED_COST'] > 50000]
    #new_renovations = new_large_permits[new_large_permits['PERMIT_TYPE'] == 'PERMIT - RENOVATION/ALTERATION']
    #new_new_constructions = new_large_permits[new_large_permits['PERMIT_TYPE'] == 'PERMIT - NEW CONSTRUCTION']

    #new_renovations.to_csv(renovations_file_path, index=False)
    #new_new_constructions.to_csv(new_constructions_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')