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

edit = Blueprint('APP_edit', __name__)
@edit.route('/message/edit', methods = ['PUT'])
def message_edit():

    message = request.form.get('message')
    message_id = request.form.get('message_id')
    token = request.form.get('token')

    if token_check(token) == False:
        raise AccessError('Invalid Token')
    
    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']    
    
    global data
    data = getData()

    # search for the channels the user is appart of 
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
#all channels user is apart of
all_channels = channels_list(token)
for channel in all_channels:
    #for each channel get the channel id
    variable_channel_id = channel.get("id")
    #for each channel id get the channel details
    variable_channel_details = channel_details(token, variable_channel_id)
    #extract the list of dictionaries of channel owners for the specified channel
    variable_channel_owners = variable_channel_details.get("owner_members")
    #initialise channel messages and a variable i
    i = 0
    variable_all_messages_dict = {'end': 0}
    #while you havent reached the end of the channel messages
    while variable_all_messages_dict.get("end") != -1:
        #extract the first 50 channel messages, start index and end index
        variable_all_messages_dict = channel_messages(token, variable_channel_id, i)
        i += 50
        #extract just the messages dictionary without the start/end index
        varirable_all_messages = variable_all_messages_dict.get("messages")
        #find the target message you want to edit in
        target_message = next((item) for item in variable_all_messages if item["message_id"] == message_id, '-1')
        #if could not find target message continue to next iter in loop
        if target_message == '-1':
            continue
        #if found message, get the user id of that message
        user_id = target_message.get('u_id')
        #check to see if the user id of that message is apart of the owners list of this particular channel
        is_owner = any(user_id in owners for owners in variable_channel_owners)
        #if satisfy error conditions, raise an error
        if user_id != uid_3 and is_owner == False:
            raise ValueError("Not an authorised user")
        #if no errors, overwrite old message with new one (IMPLEMENTATION)\\\
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        for d in data['channels']['messages']:
            if d['message_id'] == message_id:
                d['message'] = message
                d['time_created'] = currentTime
                break

return {}
'''
