from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *
from uid_check import *
from channel_check import *

details = Blueprint('details',__name__) 
@details.route('/channel/details', methods=['GET'])
def channel_details():

    global data
    data = getData()

    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))
    
    if id_check(channel_id) == False:
        raise ValueError("invalid channel id")
    #print("get here")  
    if member_check(token, channel_id) == False:
        raise AccessError("Authorised user is not a member of this channel.")
    #print("get here 2")

    ret = {
        'name': data['channel_details'][channel_id]['name'],
        'owner_members': [],
        'all_members': []
    }
    
    # get the names of the members
    for i, item in data['users'].items():
        if item['u_id'] in data['channel_details'][channel_id]['all_members']:
            if item['u_id'] in data['channel_details'][channel_id]['owner_members']:
                # add to owners
                ret['owner_members'].append(  {'u_id': item['u_id'], 'name_first': item['name_first'], 'name_last': item['name_last'] })
            else:
                # add to all
                ret['all_members'].append(  {'u_id': item['u_id'], 'name_first': item['name_first'], 'name_last': item['name_last'] })  
    print(ret)  
    return dumps(ret)
