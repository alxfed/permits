# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot


def main():
    parameters = {
                    'name': '',
                    'type':'PROSPECT',
                    'phone':'',
                    'address':'',
                    'city':'',
                    'state':'',
                    'zip': '',
                    'category':'General Contractor'
                  }

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

    not_lic_file_path = '/home/alxfed/archive/not_licensed_contractors.csv'

    seen = set()
    not_lic = []
    for indx, contractor in contractors.iterrows():
        company = contractor['general_contractor']
        if company not in seen:
            licensed = gen_contractors['company_name'].values
            if company in licensed:
                seen.add(company)
                pass
            else:
                not_lic.append(company)
        else:
            pass
    not_licensed = pd.DataFrame(not_lic)
    not_licensed.to_csv(not_lic_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')