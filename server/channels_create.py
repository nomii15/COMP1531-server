#definition channels_create function
from flask import Flask, request, Blueprint

# importing the data file
from data import *

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''
# maybe need to change route - double check later
@APP.route('channels/create', methods['POST'])
def channels_create(token, name, is_public):
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

    # also need to add to channel details 
    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()

    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    data['channel_details'][channel] = {'name' : name, 'owner_members' : [token_payload['u_id']], 'all_members' : [token_payload['u_id']]}

    return channel_id