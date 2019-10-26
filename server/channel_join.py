#definition channels_listall function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError
import jwt

# importing the data file
from data import *
from token_check import *

from uid_check import *
from channel_check import *



'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''


join = Blueprint('join', __name__)
@join.route('/channel/join', methods=['POST'])

def channel_join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    if token_check(token) == False:
        raise AccessError('Invalid Token')

    if id_check(channel_id):
        raise ValueError("channel_id does not refer to a valid channel that the authorised user is part of.")
        

    global SECRET    
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms='HS256')
    u_id = Payload['u_id'] 

    if uid_check(u_id) == False:
        raise ValueError("invalid u_id.")      

    global data
    data = getData()

    global SECRET
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']


    # value error when channel does not exist

    for i, channel in data['channels'].items():
        print(channel)
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channel_details'][int(channel_id)]['all_members'].append(ret)
                    return dumps({})
            # if get to end of this loop, user isnt valid

    # if here channel doesnt exist                

