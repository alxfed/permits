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
    auth_str = username + ':' + password
    auth = base64.b64encode(auth_str.encode())
    # header Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    head = 'Basic ' + auth.decode()
    header = {'Authorization': head}
    au = HTTPBasicAuth(username, password)
    res = requests.get(url=url, auth=(username, password))
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')