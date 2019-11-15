'''
Given a users tokenID and a message Id, remove that message

Value Errors-
    1. message_id does not exist
Access Errors-
    1. message_id not sent by the user making the request
    2. message_id corresponds to a user who is not an owner
    2. message_id corresponds to a user who is not an admin
'''
from flask import Flask, request, Blueprint
from json import dumps
from data import *
import jwt
from Error import AccessError
from token_check import token_check
from check_channel_owner import channel_owner
from token_to_uid import token_to_uid

def message_remove(token, message_id):

    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)  
    u_id = token_to_uid(token)
    # go find the channel and the message that corresponds to it
    for i,items in data['channels'].items():
        for item in items['messages']:
            if item['message_id'] == int(message_id):
                if channel_owner(items['name'], u_id) == True or item['uid'] == u_id:
                    data['channels'][i]['messages'].remove(item)
                    return dumps({})
                else:
                    ret = {
                        "code" : 400,
                        "name": "AccessError",
                        "message" : "You are not the owner of the channel or the creator of the message",
                    }
                    return dumps(ret)

    ret = {
        "code" : 400,
        "name": "ValueError",
        "message" : "The message you are trying to remove no longer exists",
    }
    return dumps(ret)



remove = Blueprint('remove', __name__)
@remove.route('/message/remove', methods = ['DELETE'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')

    return dumps(message_remove(token, message_id))
