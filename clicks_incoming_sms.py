# -*- coding: utf-8 -*-
"""poll the SMS inbox, then erase it
"""
import requests
import base64
from os import environ


def ingest_list(thelist):
    for line in thelist:
        pass
    return


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
        ingest_list(message_list)
        for page in range(2, last_page+1):
            # request the other pages and deal with their message_lists
            param = {'page': page}
            msg_list = requests.get(INBOUND_INBOX_URL, auth=(username, password), params=param).json()['data']['data']
            ingest_list(msg_list)
    else:
        return
    auth_str = base64.b64encode(f'{username}:{password}'.encode())
    headers = {'Authorization': 'Basic ' + auth_str.decode()}
    DELETE_MESSAGES_URL = 'https://rest.clicksend.com/v3/sms/inbound-read'
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