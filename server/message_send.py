'''
Given a users tokenID, send the message stored in the message parameter to the channel_id.

Value Errors-
    1. message being sent is greater than 1000 characters.
'''
from flask import Flask, request, Blueprint
from json import dumps
from channels_list import channels_list
from data import *
from datetime import datetime
from Error import AccessError
from token_check import token_check

send = Blueprint('APP_send', __name__)
@send.route('message/send', methods = ['POST'])
def message_send():

    message = request.form.get('message')
    if (len(message) > 1000):
        raise ValueError("Message too long")

    global data
    data = getData()

    token = request.form.get('token')

    if token_check(token) == False:
        raise AccessError('Invalid Token')
    
    
    channel_id = request.form.get('channel_id')
    channels_list =  channels_list(token)
    #search list of dictionaries to see if channel id you want to send a message to is in the list of authorised channels
    if not any(d['channel_id'] == channel_id for d in channels_list):
        print('Access error')
        return
    
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    reacts = []
    is_pinned = False
    message_id = len(data['channels']['messages']) + 1
    
    #extract u_id from token
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']
    
    new_message = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': currentTime,
        'reacts': reacts,
        'is_pinned': is_pinned
    }
    for d in data['channels']:
        if d['channel_id'] == channel_id:
            d['messages'].append(new_message)
            break

    return {message_id}

