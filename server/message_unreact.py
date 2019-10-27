'''
Given a users tokenID and a message Id and a react_id, unreact to a message

Value Errors-
    1. message_id not a valid message
    2. react_id is not valid
    2. message not reacted to
'''


from flask import Flask, request, Blueprint
from json import dumps
from data import *
from Error import AccessError
from token_check import token_check

from channels_list import channels_list
from channel_messages import channel_messages

unreact = Blueprint('APP_unreact', __name__)
@unreact.route('message/unreact', methods = ['POST'])
def message_unreact():

    token = request.form.get('token')
    if token_check(token) == False:
        raise AccessError('Invalid Token')

    global data
    data = getData()

    react_id = request.form.get('react_id')
    if not any(d['react_id'] == react_id for d in data['reacts']):
        raise ValueError('Invalid react id')

    for d in data['reacts']:
        if d['react_id'] == react_id and d['is_this_user_reacted'] == False:
            raise ValueError('Cannot unreact Error')


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
        while variable_all_messages_dict.get("end") != -1:\
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
            else:
                for d in data['channels']['messages']:
                    if d['message_id'] == message_id:
                        d['reacts'].remove(react_id)
                for d in data['reacts']:
                    if d['react_id'] == react_id:
                        d['u_ids'].remove(token) #have to append u_id
                        d['is_this_user_reacted'] = False
                
                n -= 1
                break
            break

    #if all the channels have been searched, this means no message has been found
    #need to decrement n once in implementation to not accidently call error in the case the message is found in the last channel search
    if n == number_of_channels:
        raise ValueError("Invalid messageId")

    return {}