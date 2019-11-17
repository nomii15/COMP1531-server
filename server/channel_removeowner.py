'''
Remove user with user id u_id as an owner of this channel

ValueError when:
    Channel (based on ID) does not exist
    When user with user id u_id is not an owner of the channel

AccessError when:
    The authorised user is not an owner of the slackr, or an owner of this channel

'''

from email_check import email_check
from flask import Flask, request, Blueprint
from json import dumps
import jwt
from Error import *

# importing the data file
from data import *

removeowner = Blueprint('removeowner', __name__)
@removeowner.route('/channel/removeowner')
def Removeowner():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))
    return dumps(channel_removeowner(token, channel_id, u_id))

def channel_removeowner(token, channel_id, u_id):
    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')

    #exceptions
    if member_check(token, channel_id) == False:
        raise AccessError(description = "inviter is not a member of the given channel.")

    if id_check(channel_id):
        raise ValueError(description = "channel_id does not refer to a valid channel that the authorised user is part of.")

    if uid_check(u_id) == False:
        raise ValueError(description = "invalid u_id.")

    # all valid, remove u_id from owner channel
    for i, channel in data['channels'].items():
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channels'][channel_id]['owner_members'].remove(ret)
                    return {}