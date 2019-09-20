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
    INP_FILE = '/home/alxfed/dbase/new_construction_scraped.jl'
    OUT_FILE = '/home/alxfed/dbase/new_construction_procssd.jl'
    #df = read_into_pd(INP_FILE)
    #res = write_pd_to_jl(df, OUT_FILE)
    with jsonlines.open(INP_FILE, mode='r') as reader:
        with jsonlines.open(OUT_FILE, mode='a') as writer:
            for line in reader:
                full_address = line['full_address']
                input_address = line['input_address']
                range_address = line['range_address']
                insp_table = pd.DataFrame.from_records(line['insp_table'])
                perm_table = pd.DataFrame.from_records(line['perm_table'])
                # transform
                writer.write(line)
        writer.close()
    reader.close()
    return


if __name__ == '__main__':
    main()
    print('main - done')