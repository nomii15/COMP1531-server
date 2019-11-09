from data import *
from flask import Flask, request, Blueprint
from json import dumps
from token_check import token_check
from channel_check import id_check

def standup_active(token, channel_id):
    if token_check(token) == "Invalid_token":
        raise ValueError("Invalid Token")

    # check channel id
    if id_check(channel_id)==False:
        raise ValueError("Invalid Channel ID")

    # by default, is active is false and time finish is none when 
    # channel is created, only when standup start is 
    # called when these variables change
    return {    
        'is_active': data['channels'][channel_id]['standup_active'],
        'time_finish': data['channels'][channel_id]['time_finish']    
    }


active = Blueprint('active', __name__)

@active.route('/standup/active', methods=['GET'])
def route():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))
    print(token, channel_id)
    return dumps( standup_active(token, channel_id) )
