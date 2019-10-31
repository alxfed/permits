# -*- coding: utf-8 -*-
"""https://www.chicago.gov/city/en/depts/bldgs/provdrs/gen_contract.html
"""
import pandas as pd
import numpy as np
from numpy import nan


def compare_with_companies_and_state(row, present, reference):
    # reference - existing companies
    # present - existing deals
    # row - permit
    to_add = {}
    not_to_add = {}
    this_permit_number = row['permit_']
    numbers_in_existing_deals = present['permit_'].values
    if this_permit_number not in numbers_in_existing_deals:
        found = reference[reference['name'].str.find(sub=row['general_contractor']) != -1]
        if found.empty:
            # TODO: add to not_to_add
            print('ok')
            pass
        else:
            companyId = found['companyId'].values[0]
            # TODO: create a deal and associate it with this companyId
            # TODO: if success - add to to_add
            # TODO: if not success - add to not_to_add
            pass
    return to_add, not_to_add



def main():
    # active General Contractors are on https://webapps1.chicago.gov/activegcWeb/
    origin_file_path                = '/home/alxfed/archive/general_contractors_doing_renovations_and_their_permits.csv'
    permit_useful_columns           = ['general_contractor', 'id', 'permit_', 'permit_type',
                                       'application_start_date', 'issue_date',
                                       'street_number', 'street_direction', 'street_name', 'suffix',
                                       'work_description', 'reported_cost']
    companies_file_path             = '/home/alxfed/archive/companies_downloaded.csv'
    companies_columns               = ['companyId', 'isDeleted', 'name', 'phone', 'phone_mobile', 'phone_voip',
                                       'phone_toll', 'phone_landline', 'phone_unidentified',
                                       'address', 'city', 'zip', 'state', 'category', 'website']
    present_state_file_path         = '/home/alxfed/archive/deals_downloaded.csv'
    present_state_columns           = ['dealId', 'isDeleted', 'associatedVids', 'associatedTicketIds',
                                       'associatedCompanyIds', 'associatedDealIds', 'dealname',
                                       'closedate', 'amount', 'pipeline', 'dealstage',
                                       'permit_issue_date', 'permit_', 'permit', 'permit_type',
                                       'work_descrption']
    general_contractors_file_path   = '/home/alxfed/archive/licensed_general_contractors.csv'
    output_file_path                = '/home/alxfed/archive/created_deals_for_ra_permits.csv'
    not_created_file_path           = '/home/alxfed/archive/not_created_deals_in_ra_permits.csv'

    input_perm      = pd.read_csv(origin_file_path, dtype=object)
    present_state  = pd.read_csv(present_state_file_path, dtype=object)
    companies    = pd.read_csv(companies_file_path, dtype=object)
    companies['name'] = companies['name'].str.upper()

    # prepare for the output
    out = []
    not_crtd = []

    for index, this_permit in input_perm.iterrows():
        to_add, not_to_add = compare_with_companies_and_state(this_permit, present_state, companies)
        if to_add:
            # modDfObj = dfObj.append(pd.Series(['Raju', 21, 'Bangalore', 'India'], index=dfObj.columns ), ignore_index=True)
            out.append(to_add)
        if not_to_add:
            not_crtd.append(not_to_add)

    # output
    output = pd.DataFrame(out)
    if not output.empty:
        output.to_csv(output_file_path, index=False)

    not_created = pd.DataFrame(not_crtd)
    if not not_created.empty:
        not_created.to_csv(not_created_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')