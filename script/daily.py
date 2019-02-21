#!/usr/bin/env python
import datetime
from httplib2 import Http
from json import dumps, loads
import os

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    http_obj = Http()
    url = os.environ['chat_url']
    
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
