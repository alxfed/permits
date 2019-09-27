# -*- coding: utf-8 -*-
"""...
"""
import requests
import base64
from os import environ


def main():
    username = environ['USER_NAME'] # 'Aladdin'
    password = environ['API_KEY'] # 'open sesame'
    auth_str = username + ':' + password
    auth = base64.b64encode(auth_str.encode())
    # header Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')