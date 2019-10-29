# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    stage_values_to_names = {'815586': 'Permit Issued',
                             '192335': 'Received layout - Make Quote',
                             '304544': 'Ready for production',
                             '904851': 'Clients (come in)',
                             '874022': 'Uploaded',
                             '815587': 'General Contractor Contacted',
                             'a17034a6-c5ef-4442-838d-c65f94c85ebd': 'Quote sent out',
                             '0899a41f-47bc-4eb7-b524-20f330e4afd0': 'In production',
                             'bd8039e1-8b13-4840-a5cb-95c9aff3067c': 'Received layout - Make quote',
                             '874023': 'Company / Contacts contacted'}
    DOWNLOADED_DEALS_FILE_PATH = '/home/alxfed/archive/deals_downloaded.csv'
    request_params = ['dealname', 'closedate', 'amount', 'pipeline', 'dealstage']
    # my pipeline is 815585 , stage 815586
    include_associations = True
    all_deals_cdr, all_columns = hubspot.deals.get_all_deals(request_params, include_associations)
    with open(DOWNLOADED_DEALS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(all_deals_cdr)
    return


if __name__ == '__main__':
    main()
    print('main - done')