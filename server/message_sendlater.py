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

from datetime import datetime

from channels_list import channels_list
from message_send import message_send

@APP.route('message/sendlater', methods = ['POST'])
def message_sendlater(token, channel_id, message, time_sent):
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')

    subscribedChannels = channels_list(token)
    if channel_id not in subscribedChannels:
        raise ValueError("Invalid Channel ID")

    if len(message) > 1000:
        raise ValueError("The message you are trying to send is too large")
    
    if time_sent < datetime.now().time():
        raise ValueError("The time you selected is in the past")

    global data
    data = getData()

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")

    while currentTime != time_sent:
        pass

    message_id = message_send(token, channel_id, message)

    return {message_id}

if __name__ == '__main__':
    APP.run(port=20000)
