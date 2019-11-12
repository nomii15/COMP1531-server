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

remove = Blueprint('APP_remove', __name__)
@remove.route('/message/remove', methods = ['DELETE'])
def message_remove():
    
    message_id = request.form.get('message_id')
    token = request.form.get('token')

    if token_check(token) == False:
        raise AccessError('Invalid Token')

    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']    

    # go find the channel and the message that corresponds to it
    for i,items in data['channels'].items():
        print(items)
        for item in items['messages']:
            print(item)
            if item['message_id'] == int(message_id):
                data['channels'][i]['messages'].remove(item)
                return dumps({})

'''   
global data
data = getData()
#all channels user is apart of
all_channels = channels_list(token)
#number of channels user is apart of
number_of_channels = len(all_channels)
n = 0
for channel in all_channels:
    #increment to keep track of number of searched channels
    n += 1
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
        target_message = next(item for item in variable_all_messages if item["message_id"] == message_id, '-1')
        #if could not find target message continue to next iter in loop
        if target_message == '-1':
            continue
        #if found message, get the user id of that message
        user_id = -1
        user_id = target_message.get('u_id')
        #check to see if the user id of that message is apart of the owners list of this particular channel
        is_owner = any(user_id in owners for owners in variable_channel_owners)
        #if satisfy error conditions, raise an error
        if user_id != uid_3 and is_owner == False:
            raise ValueError("Not an authorised user")
        for d in data['channels']['messages']:
            if d['message_id'] == message_id:
                del data['channels'][d]
                break
if n == number_of_channels and user_id == -1:
    raise ValueError("Message could not be found")

return {}
'''