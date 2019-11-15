'''
Given a users tokenID and a message Id, pin the message

Value Errors-
    1. message_id not a valid message
    2. authorised user is not an admin
    3. message already pinned
AccessError-
    1. Authorised user is not a memeber of channel
'''
from flask import Flask, request, Blueprint
from json import dumps
from data import *
from Error import AccessError
from token_check import token_check
from check_channel_owner import channel_owner
import jwt
from token_to_uid import token_to_uid

def message_pin(token, message_id):
    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    
    global data
    data = getData()
    uid = token_to_uid(token)

    # find the message and modify the pin operation
    for i, items in data['channels'].items():
        for item in items['messages']:
            if item['message_id']==int(message_id):
                #only if user is an admin - need to use channel_id instead of channel_name inn the channel owner check below
                if channel_owner(items['name'], uid) == True:
                    # got the message, check its pin
                    if item['is_pinned'] == False:
                        item['is_pinned'] = True
                        return dumps({})
                    else:
                        ret = {
                            "code" : 400,
                            "name": "ValueError",
                            "message" : "Message is already pinned",
                        }
                        return dumps(ret)
                else:
                    ret = {
                        "code" : 400,
                        "name": "ValueError",
                        "message" : "The authorised user is not an admin",
                    }
                    return dumps(ret)

    #if you get to this logic, means you couldnt find message with messageId
    ret = {
        "code" : 400,
        "name": "ValueError",
        "message" : "Could not find message, with message Id",
    }
    return dumps(ret)   
                

pin = Blueprint('pin', __name__)
@pin.route('/message/pin', methods = ['POST'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')

    return dumps(message_pin(token, message_id))
