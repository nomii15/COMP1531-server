#definition channels_list function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError

# importing the data file
from data import *
from token_check import *
from token_to_uid import token_to_uid

'''
Provide a list of all channels (and their associated details) that the authorised user is part of

'''
Channels_list = Blueprint('Channels_list', __name__)
@Channels_list.route('/channels/list', methods=['GET'])
def List():
    token = request.args.get('token')
    return dumps(channels_list(token))

def channels_list(token):
    # search through data['channel_details'][channels]
    # for each channel, check if user is existing as a member
    # if a member, add channel id to list
    # return data['channel_details'][list]

    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')
    
    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    #extract u_id from token
    u_id = token_to_uid(token)

    channelret = []

    #for each channel, check if user is a member
    for i,channel in data['channel_details'].items():
        #print(channel)
        for j in channel['all_members']:
            if j['u_id'] == u_id:
                channelret.append({'channel_id': i, 'name': channel['name']})

    ret = {'channels': channelret} 

    return ret
        
