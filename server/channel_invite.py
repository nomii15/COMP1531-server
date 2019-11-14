from json import dumps
from flask import request, Blueprint
from data import *
from uid_check import *
from channel_check import member_check, id_check

INVITE = Blueprint('INVITE', __name__)

@INVITE.route('/channel/invite', methods=['POST'])
def channel_invite_route():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))
    return dumps(channel_invite(token, channel_id, u_id))

def channel_invite(token, channel_id, u_id):
    global data
    data = getData()
    #exceptions
    if uid_check(u_id) is not True:
        raise ValueError("invalid u_id.")
    if member_check(token, channel_id) is not True:
        raise AccessError("inviter is not a member of the given channel.")
    if id_check(channel_id) is not True:
        raise ValueError("invalid channel.")
    
    new_member = {
    }
    
    for key, item in data['users'].items():
        if key == u_id:
            new_member['u_id'] = item['u_id']
            new_member['name_first'] = item['name_first']
            new_member['name_last'] = item['name_last']
    data['channel_details'][channel_id]['all_members'].append(new_member)
    return {
    }
