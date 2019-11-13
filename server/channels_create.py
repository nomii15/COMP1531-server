#definition channels_create function
from flask import Flask, request, Blueprint
import jwt
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''

Channels_create = Blueprint('Channels_create', __name__)
@Channels_create.route('/channels/create', methods=['POST'])
def channels_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')

    if token_check(token) == False:
        raise AccessError('Invalid Token')

    # channel name length check
    if len(name) > 20:
        raise ValueError("Channel name too long")

    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    global channel
    channel = getChannels()

    channel_id = channel

    data['channels'][channel] = {'channel_id': channel_id, 'name': name, 'messages': [], 'standup_active': False, 'time_finish': None, 'startup_user': None}

    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']

    detail = {}
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            detail['u_id'] = items['u_id']
            detail['name_first'] = items['name_first']
            detail['name_last'] = items['name_last']
            break



    
    # adding to channel details, registering as a member of the channel
   
    data['channel_details'][channel] = {'name' : name, 'owner_members' : [], 'all_members' : [] , 'public': is_public}
    data['channel_details'][channel]['owner_members'].append(detail)
    data['channel_details'][channel]['all_members'].append(detail)
    incChannel()
    #print(data['channel_details'])

    return dumps(channel_id)