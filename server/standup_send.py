#definition of the standup_send function
from data import *
from flask import Flask, request, Blueprint
from json import dumps
from token_check import token_check
from channel_check import id_check, member_check
from Error import AccessError
from datetime import timezone
from message_send import message_send
import jwt

'''
Sending a message to get buffered in the standup queue, assuming a standup is currently active

ValueError when:
Channel (based on ID) does not exist
Message is more than 1000 characters

AccessError when
The authorised user is not a member of the channel that the message is within
If the standup time has stopped
'''

def standup_send(token, channel_id, message):
    
    #check token
    if token_check(token) == "Invalid_token":
        raise ValueError("Invalid Token")

    # check channel id
    if id_check(channel_id)==False:
        raise ValueError("Invalid Channel ID")

    #check if member of channel
    if member_check(token, channel_id) == False:
        raise AccessError("Not a member of the channel")

    global data 
    data = getData()
    # check whether a standup is not active
    if data['channels'][channel_id]['standup_active'] == False:
        raise ValueError("Standup not active")

    # call message send to send value
    message_send(token, channel_id, message)   

    # add the message to a buffer to store
    global standup
    standup = getStandup()

    # get the user who sent it
    name = ""
    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']
    
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            name = items['name_first']

    stand_message = {
        'name': name,
        'message': message
    }

    for i in standup:
        if i['channel_id'] == channel_id:
            # if the channel id exists in the buffer, append message
            i['messages'].append(stand_message)
            return {}

    # if we get here, first message is send, create new entry and 
    new = {
        'channel_id': channel_id,
        'messages': [stand_message]
    }
    standup.append(new)
    return {}



standsend = Blueprint('standsend', __name__)
@standsend.route('/standup/send', methods=['POST'])
def startSend():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    message = request.form.get('message')
    return dumps( standup_send(token, channel_id, message)  ) 
