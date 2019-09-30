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
    INP_FILE = '/media/alxfed/toca/aa-crm/regular/downloaded/last_week_newconst.jl'
    OUT_FILE = '/media/alxfed/toca/aa-crm/regular/downloaded/last_week_newconst_sorted.jl'
    columns = ['id', 'permit', 'permit_type', 'review_type', 'application_start_date', 'issue_date', 'processing_time',
               'street_number', 'street_direction', 'street_name', 'suffix', 'work_description', 'building_fee_paid',
               'zoning_fee_paid', 'other_fee_paid', 'subtotal_paid', 'building_fee_unpaid', 'zoning_fee_unpaid',
               'other_fee_unpaid', 'subtotal_unpaid', 'building_fee_waived', 'zoning_fee_waived', 'other_fee_waived',
               'subtotal_waived', 'total_fee', 'contact_1_type', 'contact_1_name', 'contact_1_city', 'contact_1_state',
               'contact_1_zipcode', 'contact_2_type', 'contact_2_name', 'contact_2_city', 'contact_2_state',
               'contact_2_zipcode', 'contact_3_type', 'contact_3_name', 'contact_3_city', 'contact_3_state',
               'contact_3_zipcode', 'reported_cost', 'pin1', 'community_area', 'census_tract', 'ward', 'xcoordinate',
               'ycoordinate', 'latitude', 'longitude', 'location', 'contact_4_type', 'contact_4_name', 'contact_4_city',
               'contact_4_state', 'contact_4_zipcode', 'contact_5_type', 'contact_5_name', 'contact_5_city',
               'contact_5_state', 'contact_5_zipcode', 'pin2', 'contact_6_type', 'contact_6_name', 'contact_6_city',
               'contact_6_state', 'contact_6_zipcode', 'contact_7_type', 'contact_7_name', 'contact_7_city',
               'contact_7_state', 'contact_7_zipcode', 'contact_8_type', 'contact_8_name', 'contact_8_city',
               'contact_8_state', 'contact_8_zipcode', 'contact_9_type', 'contact_9_name', 'contact_9_city',
               'contact_9_state', 'contact_9_zipcode', 'contact_10_type', 'contact_10_name', 'contact_10_city',
               'contact_10_state', 'contact_10_zipcode',
               'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10']

    with jsonlines.open(INP_FILE, mode='r') as reader:
        with jsonlines.open(OUT_FILE, mode='a') as writer:
            for line in reader:
                full_address = line['full_address']

                writer.write(line)
        writer.close()
    reader.close()
    return


if __name__ == '__main__':
    main()
    print('main - done')