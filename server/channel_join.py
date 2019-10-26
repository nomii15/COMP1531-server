#definition channels_listall function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *
from channel_check import id_check

'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

channel_join = Blueprint('APP_listall', __name__)
@channel_join.route('channels/listall', methods['POST'])
def channel_join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    if token_check(token) == False:
        raise AccessError('Invalid Token')

    global data
    data = getData()

    global SECRET
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']


    # value error when channel does not exist
    if id_check(channel_id) == False:
        raise ValueError('Channel does not exist')

    # access error when channel is private
    if data['channel'][channel]['is_public'] == False:
        if u_id not in data['channel_details'][channel_id]['owner_members']:
            raise AccessError('Access denied')

    # adding to members
    data['channel_details'][channel_id]['all_members'].append(u_id)