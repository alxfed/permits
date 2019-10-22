# -*- coding: utf-8 -*-
"""...
"""
import googlemaps
import os
import time


def main():
    addre = 'D CONSTRUCTION, INC' #''
    token = os.environ['API_TOKEN']

    location = {'lat': 41.8781136, 'lng': -87.6297982}

    bias = 'circle:50000@' + str(location['lat']) + ',' + str(location['lng'])
    maps_client = googlemaps.Client(key=token, timeout=10,
                                    retry_timeout=2,
                                    queries_per_second=1,
                                    retry_over_query_limit=True)

    result = maps_client.find_place(input=addre,
                                        input_type="textquery",
                                        fields=['place_id'],
                                        location_bias=bias)
    info = result['candidates'][0]
    # address = info['formatted_address']
    # name = info['name']
    place_id = info['place_id']

    contact = maps_client.place(place_id=place_id,
                                fields=['name', 'formatted_address',
                                        'formatted_phone_number', 'website'])['result']

    print(result)

    return


if __name__ == '__main__':
    main()
    print('main - done')



