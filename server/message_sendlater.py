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


def message_sendlater(token, channel_id, message, time_sent):

    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)

    allChannels = channels_listall(token)
    if channel_id not in allChannels:
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "Could not find a channel with the specified Id",
        }
        return dumps(ret)

    subscribedChannels = channels_list(token)
    if channel_id not in subscribedChannels:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "You are not apart of the channel you are trying to post to",
        }
        return dumps(ret)
        
    if len(message) > 1000:
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "The message sent was too long",
        }
        return dumps(ret)
    
    if time_sent < datetime.now().time():
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "You cannot send a message in the past",
        }
        return dumps(ret)

    global data
    data = getData()

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")

    while currentTime != time_sent:
        pass

    message_id = message_send(token, channel_id, message)

    return dumps(message_id)


sendlater = Blueprint('APP_sendlater', __name__)
@sendlater.route('message/sendlater', methods = ['POST'])
def route():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    
    return dumps(message_sendlater(token, channel_id, message, time_sent))