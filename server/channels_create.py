#definition channels_create function
from flask import Flask, request, Blueprint
import jwt
from json import dumps

# importing the data file
from data import *
from token_check import *

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''
# maybe need to change route - double check later
@APP.route('channels/create', methods['POST'])
def channels_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')

    if token_check(token) == False:
        raise Exception('AccessError')

    # channel name length check
    if len(name) > 20:
        raise ValueError("Channel name too long")

    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    global channel
    channel = getChannels()

    channel_id = channel

    data['channels'][channel] = {'channel_id': channel_id, 'name': name}

    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()

    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])

    u_id = token_payload['u_id']
    
    # adding to channel details, registering as a member of the channel
    data['channel_details'][channel] = {'name' : name, 'owner_members' : u_id, 'all_members' : u_id}
    incChannel()

    return dumps(channel_id)