# -*- coding: utf-8 -*-
"""...
"""
import datetime as dt
import requests
import pandas as pd
from os import environ


RESOURCE_URL = 'data.cityofchicago.org'
RESOURCE_ID  = 'ydr8-5enu'                      # permits data
api_token = environ['API_TOKEN']
api_url = f'https://{RESOURCE_URL}/resource/{RESOURCE_ID}.json'
header = {'Content-Type': 'application/json', 'X-App-Token': api_token}


def data_chunk(uri):
    response = requests.get(uri, headers=header)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 201:
        raise RuntimeError("Request Processing")
    elif response.status_code == 400:
        raise RuntimeError("Bad Request")
    elif response.status_code == 401:
        raise RuntimeError("Unauthorized")
    elif response.status_code == 403:
        raise RuntimeError("Forbidden")
    elif response.status_code == 404:
        raise RuntimeError("Not Found")
    elif response.status_code == 429:
        raise RuntimeError("Too many Requests")
    elif response.status_code == 500:
        raise RuntimeError("Server Error")
    else:
        return None # silently return nothing


def main():
    """Read a chunk with date_issued in predefined window
    """
    data = pd.DataFrame()

    start_dt = dt.datetime(year=2019, month=7, day=1, hour=0, minute=0, second=0)
    start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S')
    end_dt = dt.datetime(year=2019, month=9, day=20, hour=0, minute=0, second=0)
    end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S')
    api_call = api_url + f'?$where=issue_date between "{start_str}" and "{end_str}"'

    limit = 1000  # limit of the frame within the time window
    offset = 0
    data_to_read_left = True

    while data_to_read_left:
        api_frame = api_call + f'&$limit={limit}&$offset={offset}'
        new_chunk = pd.DataFrame.from_records(data_chunk(api_frame))
        new_chunk['issue_date'] = pd.to_datetime(new_chunk['issue_date'])
        new_chunk['application_start_date'] = pd.to_datetime(new_chunk['application_start_date'])
        new_chunk['reported_cost'] = pd.to_numeric(new_chunk['reported_cost'], downcast='unsigned')
        data = data.append(new_chunk, sort=False, ignore_index = True)
        if new_chunk.id.count() == limit:
            offset += limit
        else:
            data_to_read_left = False
    new_construction = data[data['permit_type'] == 'PERMIT - NEW CONSTRUCTION']
    renovation = data[data['permit_type'] == 'PERMIT - RENOVATION/ALTERATION']
    return


if __name__ == '__main__':
    main()
    print('main - done')


'''
# long complex request

api_url = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T14:00:00'"

# date-time or "floating timestamp" are in ISO8601 Times
# https://en.wikipedia.org/wiki/ISO_8601#Times

# url string formation

api_url_base = 'data.cityofchicago.org'
api_resource_id = 'ydr8-5enu'

api_url = 'https://{}/resource/{}.json'.format(api_url_base, api_resource_id)

# but f-string for complex requests _for sure_

requ = 'where'
argu = ''

api_request = f'{api_url}?${requ}={argu}'

# but if the parameters of the query are already in a dictionary
# then the trick is:

person = {'name': 'Alex', 'age': 64}
message = "Hello, {name}. You are {age}.".format(**person)
'''