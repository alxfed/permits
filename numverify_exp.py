# -*- coding: utf-8 -*-
"""...
"""
import requests
from os import environ


def main():
    api_key = environ['KEY']
    api_url = 'http://apilayer.net/api/validate?access_key=' + api_key
    ph = '+13128048798'
    par = {'number': ph}
    resp = requests.get(api_url, params=par)
    res = resp.json()
    line_type = res['line_type']
    return


if __name__ == '__main__':
    main()
    print('main - done')