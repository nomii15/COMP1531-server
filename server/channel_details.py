from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *
from uid_check import *
from channel_check import *

App = Flask(__name__)

App.route=('channel/details', methods=['GET'])
def channel_details():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    
    if id_check(channel_id) == False:
        raise ValueError("invalid channel id")
        
    if member_check(token) == False:
        raise AccessError("Authorised user is not a member of this channel.")
        
    return dumps({
        "name": data['channel_details'][channel_id]['name']
        "owner_members": data['channel_details'][channel_id]['owner_members']
        "all_members": data['channel_details'][channel_id]['all_members']
    })
