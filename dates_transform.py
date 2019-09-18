# -*- coding: utf-8 -*-
"""ingest csv file (even if there are gaps, that's why nan is here)
and format the dates into a unix timestamp like format.
"""
import pandas as pd
from numpy import nan
from datetime import datetime, date, time


def dateparse(x):
    if x is nan:
        return None
    else:
        return pd.datetime.strptime(x, '%m/%d/%Y')


def main():
    input_file_path = '/home/alxfed/Downloads/Building_Permits.csv'
    output_file_path = '/home/alxfed/Downloads/Transformed_Building_Permits.csv'

    start_date  = datetime(2018, 12, 8, 0, 0)
    end_date    = datetime(2019, 9, 18, 0, 0)

    the_file = pd.read_csv(input_file_path,
                        parse_dates=['APPLICATION_START_DATE',
                                     'ISSUE_DATE'],
                        date_parser=dateparse,
                        dtype=object)
    the_file.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')