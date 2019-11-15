'''
Given a users tokenID, send the message stored in the message parameter to the channel_id.

Value Errors-
    1. message being sent is greater than 1000 characters.
'''
from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *
from datetime import datetime, timezone
from Error import AccessError
from token_check import token_check
from channel_check import id_check
from token_to_uid import token_to_uid

def message_send(token, channel_id, message):

    if (len(message) > 1000):
        ret = {
            "code" : 400,
            "name": "ValueError",
            "message" : "The message sent was too long",
        }
        return dumps(ret)

    global data
    data = getData()

    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    
    
    if id_check(int(channel_id)) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "You are trying to send a message to a channel you are not apart of",
        }
        return dumps(ret)


    global Message
    Message = getMessage()
    now = datetime.now()
    timestamp = now.replace(tzinfo=timezone.utc).timestamp()
    reacts = [{
        'react_id': 1,
        'u_ids': [],
        'is_this_user_reacted': False
    }]
    is_pinned = False

    u_id = token_to_uid(token)
    
    new_message = {
        'message_id': Message,
        'u_id': u_id,
        'message': message,
        'time_created': timestamp,
        'reacts': reacts,
        'is_pinned': is_pinned
    }
    
    for d,j in data['channels'].items():
        if j['channel_id'] == int(channel_id):
            data['channels'][d]['messages'].append(new_message)
            ret = {'message_id': Message}
            incMessage()
            return dumps({'message_id': Message})
            

    


send = Blueprint('send', __name__)
@send.route('/message/send', methods = ['POST'])
def route():
    message = request.form.get('message')
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    return dumps(message_send(token, channel_id, message))