#definition channel_leave function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *

'''
Given a channel ID, the user removed as a member of this channel.

ValueError when:
        Channel (based on ID) does not exist.

'''

leave = Blueprint('leave', __name__)
@leave.route('/channel/leave', methods=['POST'])
def channel_leave():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))    
   
    if token_check(token) == False:
        raise AccessError('Invalid Token')   


    global SECRET    
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms='HS256')
    u_id = Payload['u_id']    

    global data
    data = getData()

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
                    return dumps({})
            # if get to end of this loop, user isnt valid
    raise AccessError("not in channel")    
    # if here channel doesnt exist 