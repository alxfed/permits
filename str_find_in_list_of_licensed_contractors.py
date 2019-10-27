# -*- coding: utf-8 -*-
"""https://www.chicago.gov/city/en/depts/bldgs/provdrs/gen_contract.html
"""
import pandas as pd
import numpy as np
from numpy import nan


def is_not_in_this_dataframe_column(term, column, dataframe):
    what_is = 'this is what is in this column'
    return what_is


def compare_with_state_and_licenses(row, present, reference):
    company_name = ''
    address = ''
    phone = ''
    do_not_add = False
    general_contractor = row['general_contractor']
    one, sep, two = general_contractor.partition(' ')
    found = reference[reference['company_name'].str.find(sub=one) != -1]
    if found.empty:
        print('Found no licenses for  ', general_contractor, '\n')
    else:
        for index, refer in found.iterrows():
            company_name = refer['company_name']
            if company_name.startswith(general_contractor):
                # which means that company_name has license and the address and phone are in the refer row
                # time to check it against the companies in the system
                # one_co, sep, two_co = company_name.partition(' ')
                exist = present[present['name'].str.find(sub=one) != -1]
                if not exist.empty:
                    # something found, let's make sure that it is it
                    for ind, existing in exist.iterrows():
                        existing_co_name = existing['name']
                        if company_name.startswith(existing_co_name):
                            print('Yeah, the licensed contractor ',
                                  company_name, '  exists, and it is already in the system')
                            do_not_add = True
                        else:
                            # print('The licensed contractor ', company_name,
                            #      '  does not exist in the system yet')
                            do_not_add = False
                else:
                    # not in the system right now, continue with it.
                    do_not_add = False
                if not do_not_add:
                    company_name = company_name
                    address = refer['address']
                    phone = refer['phone']
                else:
                    address = ''
                    phone = ''
            else:
                # company_name = ''
                # print('There is no exact match in licenses for ', general_contractor,
                #      '  even though there are some  ', one, '  matches')
                pass
    return pd.Series([company_name, address, phone])




def main():
    # active General Contractors are on https://webapps1.chicago.gov/activegcWeb/
    origin_file_path                = '/home/alxfed/archive/gen_contractors_new_permits.csv'
    present_state_file_path         = '/home/alxfed/archive/companies_downloaded.csv'
    general_contractors_file_path   = '/home/alxfed/archive/licensed_general_contractors.csv'
    output_file_path                = '/home/alxfed/archive/new_licensed_contractors_for_permits.csv'


    origin      = pd.read_csv(origin_file_path, dtype=object)
    input_perm = origin.drop_duplicates(subset=['general_contractor'], keep='first', inplace=False)
    present_st  = pd.read_csv(present_state_file_path, dtype=object)
    licensed    = pd.read_csv(general_contractors_file_path, dtype=object)

    # prepare for the output
    out = pd.DataFrame()
    out[['company_name', 'address', 'phone']] = input_perm.apply(compare_with_state_and_licenses, axis=1,
                                                                present=present_st, reference=licensed)
    #output
    output = out[(out['company_name'] != '') & (out['address'] != '') & (out['address'] != np.nan)]
    output.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')