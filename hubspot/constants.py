# -*- coding: utf-8 -*-
"""...
"""
from os import environ


def hubspot_timestamp_from_date(date_object):
    from datetime import datetime
    date = datetime.fromisoformat(date_object)
    hubspot_timestamp = int(1000 * date.timestamp())
    return hubspot_timestamp


def date_from_hubsport_timestamp(hubspot_timestamp):
    from datetime import datetime
    date_time = datetime.fromtimestamp(int(hubspot_timestamp/1000))
    return date_time


api_key = environ['API_KEY']
# portal_id = environ['PORTAL_ID']
parameters = {'hapikey': api_key}
header = {'Content-Type': 'application/json'}

COMPANY_CREATE_URL  = 'https://api.hubapi.com/companies/v2/companies'
COMPANY_DELETE_URL  = 'https://api.hubapi.com/companies/v2/companies/'
COMPANY_UPDATE_URL  = 'https://api.hubapi.com/companies/v2/companies/'
COMPANY_SEARCH_URL  = 'https://api.hubapi.com/companies/v2/domains/'
COMPANIES_ALL_URL   = 'https://api.hubapi.com/companies/v2/companies/paged'

CONTACT_URL         = 'https://api.hubapi.com/contacts/v1/contact'
CONTACTS_ALL_URL = 'https://api.hubapi.com/contacts/v1/lists/all/contacts/all'
CONTACT_SEARCH_QUERY_URL = 'https://api.hubapi.com/contacts/v1/search/query?q='

ASSOCIATIONS_URL    = 'https://api.hubapi.com/crm-associations/v1/associations'

DEALS_ALL_URL       = 'https://api.hubapi.com/deals/v1/deal/paged'
