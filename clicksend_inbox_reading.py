# -*- coding: utf-8 -*-
"""...
"""
import requests
import base64
from os import environ
from requests.auth import HTTPBasicAuth


def main():
    INBOUND_INBOX_URL = 'https://rest.clicksend.com/v3/sms/inbound'
    username = environ['USER_NAME'] # 'Aladdin'
    password = environ['API_KEY'] # 'open sesame'
    data = requests.get(INBOUND_INBOX_URL, auth=(username, password)).json()['data']
    total = data['total']
    per_page = data['per_page']
    current_page = data['current_page']
    last_page = data['last_page']
    message_list = data['data']
    if total > 0:
        # deal with a message_list
        for page in range(2, last_page+1):
            # request the other pages and deal with their message_lists
            parameters = {'page': page}
            data = requests.get(INBOUND_INBOX_URL, auth=(username, password), params=parameters).json()['data']
            pass
    else:
        return
    auth_str = base64.b64encode(f'{username}:{password}'.encode())
    headers = {'Authorization': 'Basic ' + auth_str.decode()}
    DELETE_MESSAGES_URL = 'https://rest.clicksend.com/v3/sms/inbound-read'
    '''
    date_before = 1569587570
    parameters = {'date_before': date_before}
    '''
    try:
        resp = requests.put(DELETE_MESSAGES_URL, headers=headers)
        if resp.status_code == 200:
            print('Ingested messages deleted')
    except requests.exceptions.RequestException as e:
        raise e
    return


if __name__ == '__main__':
    main()
    print('main - done')