# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def create_engagement(parameters):

    data = {"engagement": {
                    "active": 'true',
                    "ownerId": 1,
                    "type": "NOTE",
                    "timestamp": 1409172644778
                },
                "associations": {
                    "contactIds": [2],
                    "companyIds": [ ],
                    "dealIds": [ ],
                    "ownerIds": [ ]
                },
                "attachments": [
                    {
                        "id": 4241968539
                    }
                ],
                "metadata": {
                    "body": "note body"
                }
            }
    list_of_properties = []
    for key in row:
        prop = {"name": hubspot_mapping[key],
                "value": row[key]}
        list_of_properties.append(prop)
    data['properties'] = list_of_properties
    response = requests.request("POST", url=COMPANIES_URL, json=data,
                                headers=constants.header, params=constants.parameters)
    if response.status_code == 200:
        row.update({'companyId': response.json()['companyId']})
        writeln(line_by_line_path, row_to_write=row)
        output_rows.append(row)
        indx += 1
        print('ok', indx)
    else:
        print('not ok! ', response.status_code)

    return



def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')