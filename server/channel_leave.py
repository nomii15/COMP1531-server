#definition channel_leave function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *
from channel_check import id_check
from token_to_uid import token_to_uid

'''
Given a channel ID, the user removed as a member of this channel.

ValueError when:
        Channel (based on ID) does not exist.

'''


leave = Blueprint('leave', __name__)
@leave.route('/channel/leave', methods=['POST'])
def Leave():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))    
    return dumps(channel_leave(token, channel_id))

def channel_leave(token, channel_id):
    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')   

    if id_check(channel_id) == False:
        raise ValueError(description = "Invalid channel_id")
    
    global data
    data = getData()

    # get uid from token
    u_id = token_to_uid(token)


    # value error when channel does not exist
    for i, channel in data['channels'].items():
        print(channel)
        if channel['channel_id'] == channel_id:
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']

                    data['channel_details'][channel_id]['all_members'].remove(ret)
                    data['channel_details'][channel_id]['owner_members'].remove(ret)
                    print(data['channel_details'][channel_id]['all_members'])
                    print(data['channel_details'][channel_id]['owner_members'])
                    return {}

