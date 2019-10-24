#definition channels_list function
from flask import Flask, request, Blueprint
from json import dumps

# importing the data file
from data import *
from token_check import *

'''
Provide a list of all channels (and their associated details) that the authorised user is part of

'''
channels_list = Blueprint('APP_create', __name__)
@channels_list.route('channels/list', methods['GET'])
def channels_list():
    # search through data['channel_details'][channels]
    # for each channel, check if user is existing as a member
    # if a member, add channel id to list
    # return data['channel_details'][list]
    token = request.form.get('token')
    if token_check(token) == False:
        raise Exception('AccessError')
    
    #add channel dictionary to add to global dictionary
    global data
    data = getData()

    #extract u_id from token
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']

    channel_list = []

    #for each channel, check if user is a member
    for channel in data['channel_details']:
        if u_id in data['channel_details'][channel]['all_members']:
            channel_list.append(channel)
    
    ret = dict()

    for channel in channel_list:
        del data['channel'][channel]['messages']
        ret[channel] = data['channel'][channel]#[['name']['channel_id']] <= check how to only return these two fields 
    
    return dumps(ret)
        
