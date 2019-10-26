from flask import Flask, request, Blueprint
from json import dumps
from data import *
from uid_check import *
from channel_check import *


invite = Blueprint('invite',__name__)


@invite.route('/channel/invite', methods=['POST'])
def channel_invite():
    global data
    data = getData()
    token = request.form.get('token')

    channel_id = int(request.form.get('channel_id'))
    invitee = request.form.get('u_id')

    
    
    
    if member_check(token, channel_id) == False:
        raise AccessError("inviter is not a member of the given channel.")
        
    if id_check(int(channel_id)):
        raise ValueError("channel_id does not refer to a valid channel that the authorised user is part of.")
        
    if uid_check(int(u_id)) == False:
        raise ValueError("invalid u_id.")

    # value error when channel does not exist
    for i, channel in data['channels'].items():
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channels'][channel_id]['all_members'].append()
                    return dumps({})
            # if get to end of this loop, user isnt valid

    # if here channel doesnt exist                



