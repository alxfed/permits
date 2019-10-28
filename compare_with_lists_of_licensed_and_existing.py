# -*- coding: utf-8 -*-
"""https://www.chicago.gov/city/en/depts/bldgs/provdrs/gen_contract.html
"""
import pandas as pd
import numpy as np
from numpy import nan


def compare_with_licenses_and_state(row, present, reference):
    company_name = ''
    address = ''
    phone = ''
    do_not_add = False
    found_to_add = {}
    unlicensed = {}
    general_contractor = row['general_contractor']
    one, sep, two = general_contractor.partition(' ')
    found = reference[reference['company_name'].str.find(sub=one) != -1]
    if found.empty:
        print('\n\nFound no licenses for  ', general_contractor, '\n\n')
        unlicensed = {'company_name': general_contractor, 'address': '', 'phone': ''}
        return found_to_add, unlicensed
    else:
        for index, refer in found.iterrows():
            company_name = refer['company_name']
            if company_name.startswith(general_contractor):
                # which means that company_name has license and the address and phone are in the refer row
                found_to_add = {'company_name': company_name,
                                'address': str(refer['address']).replace(u'\xa0', u' '),
                                'phone': refer['phone'].replace('x', '')}
                unlicensed = {}
                break
            else:
                unlicensed = {'company_name': general_contractor, 'address': '', 'phone': ''}
                return found_to_add, unlicensed

    exist = present[present['name'].str.find(sub=one) != -1]
    if not exist.empty:
        # something found, let's make sure that it is it
        for ind, existing in exist.iterrows():
            existing_co_name = existing['name']
            if company_name.startswith(existing_co_name):
                print('The licensed contractor ',
                      company_name, '  exists, and it is already in the system\n')
                found_to_add = {}
                return found_to_add, unlicensed

    return found_to_add, unlicensed


def main():
    # active General Contractors are on https://webapps1.chicago.gov/activegcWeb/
    origin_file_path                = '/home/alxfed/archive/general_contractors_doing_renovations_and_their_permits.csv'
    present_state_file_path         = '/home/alxfed/archive/companies_downloaded.csv'
    general_contractors_file_path   = '/home/alxfed/archive/licensed_general_contractors.csv'
    output_file_path                = '/home/alxfed/archive/new_licensed_contractors_for_ra_permits.csv'
    unlicensed_file_path            = '/home/alxfed/archive/unlicensed_contractors_in_ra_permits.csv'

    origin      = pd.read_csv(origin_file_path, dtype=object)
    input_perm = origin.drop_duplicates(subset=['general_contractor'], keep='first', inplace=False)
    present_st  = pd.read_csv(present_state_file_path, dtype=object)
    present_st['name'] = present_st['name'].str.upper()
    licensed    = pd.read_csv(general_contractors_file_path, dtype=object)

    # prepare for the output
    out = []
    unlicen = []

    for index, permit_holder in input_perm.iterrows():
        to_add, unlic = compare_with_licenses_and_state(permit_holder, present_st, licensed)
        if to_add:
            # to_a = pd.DataFrame(to_add)
            out.append(to_add)
        if unlic:
            unlicen.append(unlic)

    # output
    # out[['company_name', 'address', 'phone']] = input_perm.apply(compare_with_state_and_licenses, axis=1,
    #  present=present_st, reference=licensed)
    out = pd.DataFrame(out)
    output = out[(out['company_name'] != '') & (out['address'] != '') & (out['address'] != np.nan)]
    output = output.drop_duplicates(subset=['company_name'], keep='first', inplace=False)
    output.to_csv(output_file_path, index=False)

    unlicensed = pd.DataFrame(unlicen)
    unlicensed = unlicensed.drop_duplicates(subset=['company_name'], keep='first', inplace=False)
    unlicensed.to_csv(unlicensed_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')