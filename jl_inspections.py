# -*- coding: utf-8 -*-
"""https://jsonlines.readthedocs.io/en/latest/
"""
import jsonlines
import pandas as pd


def read_into_pd(inpfile):
    data = pd.read_json(inpfile, lines=True)
    return data

def write_pd_to_jl(data, outfile):
    data.to_json(outfile, orient='records', lines=True)
    return

def main():
    # renovation_alteration_scraped.jl
    INP_FILE = '/home/alxfed/dbase/renovation_alteration_scraped.jl'
    OUT_FILE = '/home/alxfed/dbase/inspections.jl'
    #df = read_into_pd(INP_FILE)
    #res = write_pd_to_jl(df, OUT_FILE)
    results = set()
    with jsonlines.open(INP_FILE, mode='r') as reader:
        for line in reader:
            insp_table = line['insp_table']
            for row in insp_table:
                if 'type_desc' in row.keys():
                    if row['type_desc'] in results:
                        pass
                    else:
                        results.add(row['type_desc'])
                else:
                    pass
    reader.close()
    return


if __name__ == '__main__':
    main()
    print('main - done')