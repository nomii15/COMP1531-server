#definition channel_leave function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *
from channel_check import id_check

'''
Given a channel ID, the user removed as a member of this channel.

ValueError when:
        Channel (based on ID) does not exist.

'''

channel_leave = Blueprint('APP_leave', __name__)
@channel_leave.route('channels/leave', methods['POST'])
def channel_leave():
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

    # removing from members
    data['channel_details'][channel_id]['all_members'].remove(u_id)