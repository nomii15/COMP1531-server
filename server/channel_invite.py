from json import dumps
from flask import request, Blueprint
from data import *
from uid_check import *
from channel_check import member_check

INVITE = Blueprint('INVITE', __name__)

@INVITE.route('/channel/invite', methods=['POST'])
def Invite()
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    u_id = request.form.get('u_id')
    return dumps(channel_invite(token, channel_id, u_id))

def channel_invite(token, channel_id, u_id):
    global data
    data = getData()

    #exceptions
    if uid_check(int(u_id)) is not True:
        raise ValueError("invalid u_id.")
    if member_check(token, channel_id) is not True:
        raise AccessError("inviter is not a member of the given channel.")
    # value error when channel does not exist
    #channel_id does not refer to a valid channel that the authorised user is part of
    for i, channel in data['channels'].items():
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channels'][channel_id]['all_members'].append(ret)
                    return ret
            # if get to end of this loop, user isnt valid
            raise ValueError("the authorised user is not part of the channel")
    # if here channel doesnt exist
    raise ValueError("the channel is not valid")