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


def message_edit(token, message_id, message):

    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    
    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']    
    
    global data
    data = getData()
    

    message_channel_id = -1
    message_channel_name = 'empty'
    is_owner = False

    #find the channel the message belongs to and check to see if message original creator(uid) is the same person who is trying to edit. if it is no need to check
    #if editor is channel owner. we can just return here
    for i, item in data['channels'].items():
        print(i)
        print('------------------------------------------')
        print(item)
        print('------------------------------------------')
        for currMessage in item['messages']:
            print(message)
            print('------------------------------------------')
            if currMessage['message_id'] == int(message_id):
                message_channel_id = i
                message_channel_name = item['name']
                if currMessage['u_id'] == u_id:
                    print('found message and the message editer is the message creator')
                    print('------------------------------------------')
                    currMessage['message'] = message
                    return dumps({})  
    

    print(f'channel id = {message_channel_id}')
    print(f'channel name = {message_channel_name}')

    #see if the editor is an owner of the channel which contains the message he is trying to edit
    for i, item in data['channel_details'].items():
        print(item)
        print(i)
        if item['name'] == message_channel_name:
            for dic in item['owner_members']:
                print("======")
                print(dic)
                if dic['u_id'] == u_id:
                    print("editor is an owner of the channel")
                    is_owner = True
  
    #if editor is an owner, find the message again and edit it.
    if is_owner == True:
        for i, item in data['channels'].items():
            print(i)
            for message in item['messages']:
                print(message)
                if message['message_id'] == int(message_id):
                    print('found message and the message editer is the owner of the channel')
                    message['message'] = message
                    return dumps({})  



edit = Blueprint('edit', __name__)
@edit.route('/message/edit', methods = ['PUT'])
def route():
    message = request.form.get('message')
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    
    return dumps(message_edit(token, message_id, message))

'''
for i, item in data['channel_details'].items():
    print(item)
    print(i)
    for dic in item['owner_members']:
    print("======")
    print(dic)
    if dic['u_id'] == u_id:
        print("part of the channel")
        #user is part of that channel, check the channel to find the message with the corresponding message id
        for j, items in data['channels'].items():
            print(items)
            print(j)
            if items['channel_id']==i:
                print("found channel, find message")
                for it in items['messages']:
                    print(it)
                    if it['message_id'] == int(message_id):
                        print("found message, modifying it")
                        it['message'] = message
                        return dumps({})    
'''