# -*- coding: utf-8 -*-
"""...
"""
from __future__ import print_function
import clicksend_client
from clicksend_client.rest import ApiException
import json
from os import environ


def main():
    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = environ['USERNAME']
    configuration.password = environ['API_KEY']

    # create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    page = 1  # int | Page number (optional) (default to 1)
    limit = 10  # int | Number of records per page (optional) (default to 10)

    try:
        # Get all inbound sms
        api_response = api_instance.sms_inbound_get(page=page, limit=limit)
        a = api_response.replace("\'", '"')
        di = dict(a)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMSApi->sms_inbound_get: %s\n" % e)
    return


if __name__ == '__main__':
    main()
    print('main - done')