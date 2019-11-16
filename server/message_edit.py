'''
Given a users tokenID and a message Id and a new message, edit the message

Value Errors-
    1. message_id not sent by the user making the request
    2. message_id corresponds to a user who is not an owner
    2. message_id corresponds to a user who is not an admin
'''
from flask import Flask, request, Blueprint
from json import dumps
from data import *
import jwt
from datetime import datetime
from Error import AccessError
from token_check import token_check
from message_remove import message_remove
from token_to_uid import token_to_uid

def message_edit(token, message_id, message):

    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    u_id = token_to_uid(token)
    
    global data
    data = getData()
    
    message_channel_id = -1
    message_channel_name = 'empty'
    is_owner = False

    #find the channel the message belongs to and check to see if message original creator(uid) is the same person who is trying to edit. if it is no need to check
    #if editor is channel owner. we can just return here
    for i, item in data['channels'].items():
        for currMessage in item['messages']:
            if currMessage['message_id'] == int(message_id):
                message_channel_id = i
                message_channel_name = item['name']
                if currMessage['u_id'] == u_id:
                    currMessage['message'] = message
                    return dumps({})  

    #see if the editor is an owner of the channel which contains the message he is trying to edit
    for i, item in data['channel_details'].items():
        if item['name'] == message_channel_name:
            for dic in item['owner_members']:
                if dic['u_id'] == u_id:
                    is_owner = True
  
    #if editor is an owner, find the message again and edit it.
    if is_owner == True:
        for i, item in data['channels'].items():
            for message in item['messages']:
                if message['message_id'] == int(message_id):
                    if message == '':
                        message_remove(token, int(message_id))
                    else:
                        message['message'] = message
                    return dumps({})

    #you would only get down to this logic if you did not create message and are not an owner
    ret = {
        "code" : 400,
        "name": "AccessError",
        "message" : "You are not the creator of the message or owner of the channel",
        }
    return dumps(ret)


edit = Blueprint('edit', __name__)
@edit.route('/message/edit', methods = ['PUT'])
def route():
    message = request.form.get('message')
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    
    return dumps(message_edit(token, message_id, message))
