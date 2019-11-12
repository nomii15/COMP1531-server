from json import dumps
from flask import request, Blueprint
import jwt
from data import *
from uid_check import *
from channel_check import *

DETAILS = Blueprint('DETAILS', __name__)
@DETAILS.route('/channel/details', methods=['GET'])
def Details():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))
    return dumps(channel_details(token, channel_id))

def channel_details(token, channel_id):
    global data
    data = getData()

    #exceptions
    if id_check(channel_id) is not True:
        raise ValueError("invalid channel id")
    if member_check(token, channel_id) is not True:
        raise AccessError("Authorised user is not a member of this channel.")
    ret = {
        'name': data['channel_details'][channel_id]['name'],
        'owner_members': [],
        'all_members': []
    }
    # get the names of the members
    for i, item in data['users'].items():
        for temp in data['channel_details'][channel_id]['all_members']:
            if item['u_id'] == temp['u_id']:
                ret['owner_members'].append({'u_id': item['u_id'], 'name_first': item['name_first'], 'name_last': item['name_last']})
        for hold in data['channel_details'][channel_id]['all_members']:
            if item['u_id'] == hold['u_id']:
                ret['all_members'].append({'u_id': item['u_id'], 'name_first': item['name_first'], 'name_last': item['name_last']})
<<<<<<< HEAD
    return dumps(ret)
=======
    return ret
>>>>>>> channel
