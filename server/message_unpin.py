'''
Given a users tokenID and a message Id, unpin the message

Value Errors-
    1. message_id not a valid message
    2. authorised user is not an admin
    3. message not pinned
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


def message_unpin(token, message_id):
    if token_check(token) == False:
        ret = {
            "code" : 400,
            "name": "AccessError",
            "message" : "Your idToken is invalid",
        }
        return dumps(ret)
    
    global data
    data = getData()

    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    uid = token_payload['u_id']

    # find the message and modify the pin operation
    for i, items in data['channels'].items():
        print(i)
        for item in items['messages']:
            if item['message_id']==int(message_id):
                print("got message id")
                if channel_owner(items['name'], uid) == True:
                    if item['is_pinned']==True:
                        item['is_pinned']=False
                        print(item)
                        return dumps({})
                    else:
                        ret = {
                            "code" : 400,
                            "name": "ValueError",
                            "message" : "Message is already already unpinned",
                        }
                        return dumps(ret)  
                else :
                    ret = {
                        "code" : 400,
                        "name": "ValueError",
                        "message" : "The authorised user is not an admin",
                    }
                    return dumps(ret) 


unpin = Blueprint('unpin', __name__)
@unpin.route('/message/unpin', methods = ['POST'])
def route():
    message_id = request.form.get('message_id')
    token = request.form.get('token')
    
    return dumps(message_unpin(token, message_id))
'''
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
        target_message = next((item) for item in variable_all_messages if item["message_id"] == message_id, '-1')
        #if could not find target message continue to next iter in loop
        if target_message == '-1':
            continue
        else:
            #if user is not an admin error/break
            if target_message.get('u_id') not in variable_channel_owners:
                raise ValueError("User is not an admin")
            #elif message is not pinned error/break
            elif target_message.get('is_pinned') == False:
                raise ValueError("Message is not pinned")
            else:
                for d in data['channels']['messages']:
                    if d['message_id'] == message_id:
                        d['is_pinned'] == False
                        n -= 1
                        break
        break
    break
#if all the channels have been searched, this means no message has been found
#need to decrement n once in implementation to not accidently call error in the case the message is found in the last channel search
if n == number_of_channels:
    raise ValueError("Invalid messageId")

return {}
    '''
