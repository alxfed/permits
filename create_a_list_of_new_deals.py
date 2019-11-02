# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot
import datetime


def main():
    properties = {
        'dealname': '',
        'dealtype':'newbusiness',
        'general_contractor':'',
        'amount': '',
        'work_descrption': '',
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
        'associatedDealIds': [],
        'associatedTicketIds': []
    }

    deals_to_create_file_path = '/home/alxfed/archive/deals_to_create_for_nc_permits.csv'
    deals_columns = ['companyId', 'general_contractor', 'issue_date', 'permit_', 'permit_type', 'reported_cost',
                     'street_direction', 'street_name', 'street_number', 'suffix', 'work_description']

    deals = pd.read_csv(deals_to_create_file_path,
                        usecols=deals_columns,
                        parse_dates=['issue_date'],
                        dtype=object)

    created_file_path = '/home/alxfed/archive/created_new_nc_deals.csv'
    not_created_file  = '/home/alxfed/archive/not_created_new_nc_deals.csv'

    created = pd.DataFrame()
    not_created = pd.DataFrame()
    for indx, deal in deals.iterrows():
        line = pd.Series()
        prop = properties.copy()
        asso = associations.copy()
        asso['associatedCompanyIds'] = [deal['companyId']]
        deal_name = str(deal['street_number']) + ' ' + str(deal['street_direction']) + ' '
        deal_name = deal_name + str(deal['street_name']) + ' ' + str(deal['suffix'])
        deal_name = 'NC ' + deal_name.title()
        prop['dealname'] = deal_name
        prop['general_contractor'] = deal['general_contractor'].title()
        prop['amount'] = .15 * float(deal['reported_cost'])
        prop['work_descrption'] = deal['work_description']
        prop['permit_'] = deal['permit_']
        prop['permit_type'] = deal['permit_type']
        prop['permit_issue_date'] = deal['issue_date'].strftime('%Y-%m-%d')
        close_date = int(deal['issue_date'].value / 1000000)
        prop['closedate'] = close_date
        crea = hubspot.deals.create_a_deal(prop, asso)
        if crea:
            line['dealId'] = str(int(crea['dealId']))
            line['isDeleted'] = str(bool(crea['isDeleted']))
            line = line.append(deal)
            created = created.append(line, ignore_index=True)
        else:
            not_created = not_created.append(deal, ignore_index=True)
    created.to_csv(created_file_path, index=False)
    not_created.to_csv(not_created_file, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')