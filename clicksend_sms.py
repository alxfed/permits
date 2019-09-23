# -*- coding: utf-8 -*-
"""Sending out a list of SMS messages
"""
from __future__ import print_function
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException
from os import environ


# Configure HTTP basic authorization: BasicAuth
configuration = clicksend_client.Configuration()
configuration.username = environ['USERNAME']
configuration.password = environ['API_KEY']


def main():
    # create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    sms_message = SmsMessage(source="sdk",
                             body="This is the body of the message.",
                             country='US',
                             to="+13129709819")
    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
    try:
        # Send sms message(s)
        api_response = api_instance.sms_send_post(sms_messages)
        sent_list = api_response['data']['messages']
        print(sent_list)
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
    return


if __name__ == '__main__':
    main()
    print('main - done')
