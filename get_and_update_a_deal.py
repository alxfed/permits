# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot


def main():
    downloaded_deals_file_path = '/home/alxfed/archive/deals_downloaded.csv'
    deals_columns = ['dealId', 'isDeleted',
                     'associatedVids', 'associatedTicketIds', 'associatedCompanyIds', 'associatedDealIds',
                     'dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
                     'permit_issue_date', 'permit_', 'permit', 'permit_type', 'work_descrption']
    reference = pd.read_csv(downloaded_deals_file_path, usecols=deals_columns, dtype=object)

    update_file_path = '/home/alxfed/archive/deals_to_update.csv'
    update_columns = ['dealId', 'isDeleted',
                     'associatedVids', 'associatedTicketIds', 'associatedCompanyIds', 'associatedDealIds',
                     'dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
                     'permit_issue_date', 'permit_', 'permit', 'permit_type', 'work_descrption']
    update_table = pd.read_csv(update_file_path, usecols=update_columns, dtype=object)

    for index, deal_to_update in update_table.iterrows():
        dealId = deal_to_update['dealId']
        gotten = hubspot.deals.get_a_deal(dealId)
        print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')