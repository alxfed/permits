# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def update_deal(companyId, parameters):
    request_url = f'{constants.COMPANY_UPDATE_URL}{companyId}'
    response = requests.request('PUT', url=request_url,
                                headers=constants.header,
                                json=parameters,
                                params=constants.parameters)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        print(response.status_code)
        return


def get_all_deals(request_parameters, include_associations):
    """Downloads the complete list of companies from the portal
    :param request_parameters: list of Contact parameters
    :param include_associations: boolean
    :return all_companies: list of dictionaries / CDR
    :return output_columns: list of output column names
    """
    # includeAssociations=true
    def make_parameters_string(include_associations, parameters_substring, offset, limit):
        authentication = 'hapikey=' + constants.api_key
        associations = ''
        if include_associations:
            associations = '&includeAssociations=true'
        parameters_string = f'{authentication}{associations}{parameters_substring}&offset={offset}&limit={limit}'
        return parameters_string
    # prepare for the inevitable output
    all_deals    = []
    output_columns  = ['dealId', 'isDeleted']
    if include_associations:
        assoc_columns = ['associatedVids', 'associatedTicketIds', 'associatedCompanyIds', 'associatedDealIds']
        output_columns.extend(assoc_columns)
    output_columns.extend(request_parameters)

    # package the parameters into a substring
    param_substring = ''
    for item in request_parameters:
        param_substring = '{}&properties={}'.format(param_substring, item)

    # prepare for the pagination
    has_more = True
    offset = 0
    limit = 250  # max 250

    # Now the main cycle
    while has_more:
        api_url = '{}?{}'.format(constants.DEALS_ALL_URL,
                                 make_parameters_string(include_associations,
                                                        param_substring,
                                                        offset, limit)
                                 )
        response = requests.request("GET", url=api_url, headers=constants.header)
        if response.status_code == 200:
            res = response.json()
            has_more    = res['hasMore']
            offset      = res['offset']
            deals       = res['deals']
            for deal in deals:
                row = {}
                row.update({"dealId"    : deal["dealId"],
                            "isDeleted" : deal["isDeleted"]
                            })
                if include_associations:
                    de_associations = deal['associations']
                    # 'associatedVids', 'associatedCompanyIds', 'associatedDealIds', 'associatedTicketIds'
                    row.update({'associatedVids'        : ' '.join(de_associations['associatedVids']),
                                'associatedCompanyIds'  : ' '.join(de_associations['associatedCompanyIds']),
                                'associatedDealIds'     : ' '.join(de_associations['associatedDealIds']),
                                'associatedTicketIds'   : ' '.join(de_associations['associatedTicketIds'])
                                })
                de_properties = deal['properties']
                for de_property in de_properties:
                    if de_property not in output_columns:
                        output_columns.append(de_property)
                        print('Adding a property to colunms list: ', de_property)
                    row.update({de_property: de_properties[de_property]['value']})
                all_deals.append(row)
            print('Now at offset: ', offset)
        else:
            print(response.status_code)
    return all_deals, output_columns


def main():
    print('You have launched this module as main')
    return


if __name__ == '__main__':
    main()
    print('main - done')