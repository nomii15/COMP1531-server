'''
Make user with user id u_id an owner of this channel

ValueError when:
    Channel (based on ID) does not exist
    When user with user id u_id is already an owner of the channel

AccessError when:
    The authorised user is not an owner of the slackr, or an owner of this channel

'''
from email_check import email_check
from flask import Flask, request, Blueprint
from json import dumps
import jwt
from Error import *
from token_check import token_check
from channel_check import member_check, id_check
from token_to_uid import token_to_uid

# importing the data file
from data import *

addowner = Blueprint('addowner', __name__)
@addowner.route('/channel/addowner')
def Addowner():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))
    return dumps(channel_addowner(token, channel_id, u_id))

def channel_addowner(token, channel_id, u_id):
    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')

    #exceptions
    if id_check(channel_id) == False:
        raise ValueError(description = "Channel_id does not refer to a valid channel that the authorised user is part of.")

    if member_check(token, channel_id) == False:
        raise AccessError(description = "Inviter is not a member of the given channel.")
        
    if uid_check(u_id) == False:
        raise ValueError(description = "Invalid u_id.")

    admin_u_id = token_to_uid(token)
    
    for j, item in data['users'].items():
        if admin_u_id == item['u_id']:
            #Checking user slackr permissions
            if item['permission'] == 3:
                raise AccessError(description = "Inviter is not an owner or admin of the slackr")

    # all valid, add u_id to owner channel
    for i, channel in data['channels'].items():
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channels'][channel_id]['owner_members'].append()
                    return {} 