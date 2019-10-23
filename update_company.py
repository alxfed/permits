# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    companyId = '627118578'
    parameters = {"properties":
                  [
                    {
                      "name": "name",
                      "value": "MBI realty"
                    }
                  ]
                 }
    result = hubspot.companies.update_company(companyId, parameters)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')