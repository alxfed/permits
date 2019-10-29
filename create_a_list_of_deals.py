# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot


def main():
    properties = {
        'dealname': '',
        'dealtype':'newbusiness',
        'description':'',
        'pipeline': '815585',
        'dealstage':'815586',
        'permit_':'',
        'permit_issue_date': '',
        'permit_type': '',
        'closedate':''
    }
    associations= {
        'associatedCompanyIds': [],
        'associatedVids': [],
        'associatedDealIds': []
    }
    comp_Id_list = associations["associatedCompanyIds"]
    cont_Id_list = associations["associatedVids"]
    deal_Id_list = associations["associatedDealIds"]

    companies_file_path = '/home/alxfed/archive/general_contractors_doing_renovations_and_their_permits.csv'
    companies_columns = ['general_contractor', 'id']
    contractors = pd.read_csv(companies_file_path,
                              usecols=companies_columns,
                              dtype=object)

    gen_cont_file_path = '/home/alxfed/archive/licensed_general_contractors.csv'
    licenses_columns = ['license_type',
                        'company_name', 'address', 'phone']
    gen_contractors = pd.read_csv(gen_cont_file_path,
                                  usecols=licenses_columns,
                                  dtype=object)

    lic_file_path = '/home/alxfed/archive/licensed_contractors_to_create.csv'

    seen = set()
    real_names = set()
    to_create = []
    for indx, contractor in contractors.iterrows():
        company = contractor['general_contractor']
        if company not in seen:
            seen.add(company)
            for ind, co_licensed in gen_contractors.iterrows():
                co_name = co_licensed['company_name']
                if co_name.startswith(company):
                    if co_name not in real_names:
                        real_names.add(co_name)
                        to_create.append(dict(co_licensed))
                        print('New name: ', co_name)
                        # and other wonderful things that have to be done
                    break
                else:
                    # licenced company doesn't start like the permit company
                    pass
        else:
            # company has been seen, do nothing
            pass
    output = pd.DataFrame(to_create)
    output.to_csv(lic_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')