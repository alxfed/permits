# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import pandas as pd
import numpy as np


def main():
    DOWNLOADED_COMPANIES_FILE_PATH = '/home/alxfed/archive/companies_downloaded.csv'
    companies_columns = ['companyId', 'isDeleted', 'name',
                         'phone', 'phone_mobile',
                         'address', 'city', 'zip', 'state', 'category', 'website']
    downl_companies = pd.read_csv(DOWNLOADED_COMPANIES_FILE_PATH,
                                    usecols=companies_columns,
                                    dtype=object)

    gen_cont_file_path = '/home/alxfed/archive/licensed_general_contractors.csv'
    licenses_columns = ['license_type',
                        'company_name', 'address', 'phone']
    gen_contractors = pd.read_csv(gen_cont_file_path,
                                    usecols=licenses_columns,
                                    dtype=object)

    for indx, company in downl_companies.iterrows():
        NAME = company['name'].upper()
        licenses = gen_contractors['company_name']
        if NAME in licenses:
            print('ok')
        pass

    companyId = '627118578'
    parameters = {"properties":
                  [
                    {
                      "name": "name",
                      "value": "MBI realty"
                    }
                  ]
                 }
    result = hubspot.companies.update_company(companyId, parameters)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')