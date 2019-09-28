# -*- coding: utf-8 -*-
"""hubspot peculiarities
"""
import datetime


def hstsnow():
    hsts = int(1000*datetime.datetime.now().timestamp())
    return hsts


def datetime_fromhsts(hsts):
    daytm = datetime.datetime.fromtimestamp(timestamp = hsts/1000)
    return daytm


def hsts_fromdatetime(datetm):
    hsts = int(1000*datetm.timestamp())
    return hsts


def main():
    hsts = hstsnow()
    dt = datetime_fromhsts(hsts)
    print(dt)
    return


if __name__ == '__main__':
    main()
    print('main - done')