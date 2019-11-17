#definition channels_create function
from flask import Flask, request, Blueprint
import jwt
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *
from token_to_uid import token_to_uid

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''

Channels_create = Blueprint('Channels_create', __name__)
@Channels_create.route('/channels/create', methods=['POST'])
def Create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    return dumps(channels_create(token, name, is_public))

def channels_create(token, name, is_public):
    if token_check(token) == False:
        raise AccessError(description = "Invalid Token")

    # channel name length check
    if len(name) > 20:
        raise ValueError(description = "Channel name too long")

    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    global channel
    channel = getChannels()

    
    channel_id = channel

    # get uid from token
    u_id = token_to_uid(token)
    # the user who calls this is the creator of the channel
    data['channels'][channel_id] = {'channel_id': channel_id, 'name': name, 'messages': [], 'standup_active': False, 'time_finish': None, 'startup_user': None}

    detail = {}
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            #add to the details of the user data and add channek_id to channel_owner in user data
            detail['u_id'] = items['u_id']
            detail['name_first'] = items['name_first']
            detail['name_last'] = items['name_last']
            break
    
    # adding to channel details, registering as a member of the channel
    # creator of the channel is also added
    data['channel_details'][channel_id] = {'channel_id' : channel_id, 'name' : name, 'owner_members' : [], 'all_members' : [] , 'public': is_public, 'creator': u_id}
    data['channel_details'][channel_id]['owner_members'].append(detail)
    data['channel_details'][channel_id]['all_members'].append(detail)
    
    incChannel()
    #print(data['channel_details'])

    return {'channel_id': channel_id}
