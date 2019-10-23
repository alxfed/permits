# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    DOWNLOADED_COMPANIES_FILE_PATH = '/home/alxfed/archive/companies_downloaded.csv'
    request_params = ['name', 'phone', 'phone_mobile', 'phone_voip',
                      'phone_toll','phone_landline','phone_unidentified',
                      'address','city','zip','state', 'category','website']
    all_companies_cdr, all_columns = hubspot.companies.get_all_companies(request_params)
    with open(DOWNLOADED_COMPANIES_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(all_companies_cdr)
    return


if __name__ == '__main__':
    main()
    print('main - done')