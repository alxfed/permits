# -*- coding: utf-8 -*-
"""...
"""
import datetime as dt
import requests
import pandas as pd
from os import environ

RESOURCE_URL = 'data.cityofchicago.org'
RESOURCE_ID  = 'ydr8-5enu'                      # permit data
api_token = environ['API_TOKEN']

api_url = f'https://{RESOURCE_URL}/resource/{RESOURCE_ID}.json'

header = {'Content-Type': 'application/json',
           'X-App-Token': api_token}


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
    '''Read a chunk with date_issued in predefined window
    '''
    start_year = 2019
    start_dt = dt.datetime(year=start_year,
                           month=7, day=1, hour=0,
                           minute=0, second=0)
    start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S')

    end_year = 2019
    end_dt = dt.datetime(year=end_year,
                         month=9, day=20, hour=0,  # the first empty day in the dataset (End of it)
                         minute=0, second=0)
    end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S')
    limit = 1000  # limit of the frame within the time window
    offset = 0  # offset of the frame within the time window

    api_frame = api_url + f'?$where=issue_date between "{start_str}" and "{end_str}"'
    # = api_call + f'&$limit={limit}&$offset={offset}'

    dst = data_chunk(api_frame)

    if dst:
        print("Here's your info: ")
        new_chunk = pd.DataFrame.from_records(dst)
        new_chunk['sale_date'] = pd.to_datetime(new_chunk['sale_date'])
    else:
        print('[!] Request Failed')
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