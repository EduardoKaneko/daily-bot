#!/usr/bin/env python
import datetime
from httplib2 import Http
from json import dumps, loads

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    http_obj = Http()
    # url = 'https://chat.googleapis.com/v1/spaces/AAAAzQuWP4o/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=V8asDvAFbzef_PxDCu0aVz4MEpqfUhqZ0d3DLVaKAro%3D'
    url = 'https://chat.googleapis.com/v1/spaces/AAAABWPOP18/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=gklA01854tZ7MXupeLAF08Yn0OWkC9wll95uS7Wm_QA%3D'
    
    # send info with bot
    bot_message = {
        'text' : f'Oie galerinha, está na hora da Daily Meeting :B',
    }
    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)

if __name__ == '__main__':
    main()