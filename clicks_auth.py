# -*- coding: utf-8 -*-
"""...
"""
import requests
import base64
from os import environ
from requests.auth import HTTPBasicAuth


def main():
    url = 'https://rest.clicksend.com/v3/sms/inbound'
    username = environ['USER_NAME'] # 'Aladdin'
    password = environ['API_KEY'] # 'open sesame'
    # binary_str = f'{username}:{password}'.encode()
    auth_str = base64.b64encode(f'{username}:{password}'.encode())
    # header Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    # basic_header = 'Basic ' + auth_str.decode()
    headers = {'Authorization': 'Basic ' + auth_str.decode()}
    # au = HTTPBasicAuth(username, password)
    n = 6
    parameters = {'page': n}
    resp = requests.get(url, headers=headers, params=parameters).json()
    message_list = resp['data']['data']
    #res = requests.get(url=url, auth=(username, password))
    # 1569587570
    url2 = 'https://rest.clicksend.com/v3/sms/inbound-read'
    date_before = 1569587570
    parameters = {'date_before': date_before}
    resp = requests.put(url2, headers=headers, params=parameters)
    res = requests.get(url=url, auth=(username, password))
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')