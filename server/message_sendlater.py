'''
Given a users tokenID, send the message stored in the message parameter to the channel_id at the specified time

Value Errors-
    1. channel_id does not exist
    2. message being sent is greater than 1000 characters.
    3. time_sent is in the past

Access Errors-
    1. not subscribed to channel_id
'''
from flask import Flask, request, Blueprint
from json import dumps
from data import *
from Error import AccessError
from token_check import token_check

from datetime import datetime
from channels_listall import channels_listall
from channels_list import channels_list
from message_send import message_send
import time


def message_sendlater(token, channel_id, message, time_sent):
    print(channel_id)
    print(message)
    print(time_sent)
    if token_check(token) == False:
        print('in token check')
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)

    global data
    data = getData()
    channel_exists = False
    for i, items in data['channels'].items():
        print(i)
        print(items)
        if i == int(channel_id):
            channel_exists = True

    if channel_exists == False:
        print('in channelid check')
        ret = {
        "code" : 400,
        "name": "ValueError",
        "message" : "Could not find a channel with the specified Id",
        }
        return dumps(ret) 

    if len(message) > 1000:
        print('in len check')
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "The message sent was too long",
        }
        return dumps(ret)
        
    print(time_sent)
    now = datetime.now()
    print(datetime.timestamp(now))
    if int(time_sent) < int(datetime.timestamp(now)):
        print('in time check')
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "You cannot send a message in the past",
        }
        return dumps(ret)

    

    timeout = int(time_sent) - int(datetime.timestamp(now))
    while int(datetime.timestamp(now)) != time_sent:
        print('in the while loop')
        time.sleep(timeout)
        print('woke up from sleep')
        message_id = message_send(token, channel_id, message)
        print(f'message id  is = {message_id}')
        return dumps(message_id)
        
    


sendlater = Blueprint('/sendlater', __name__)
@sendlater.route('/message/sendlater', methods = ['POST'])
def route():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    
    return dumps(message_sendlater(token, channel_id, message, time_sent))