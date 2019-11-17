#definition channels_listall function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError
import jwt

# importing the data file
from data import *
from token_check import *
from token_to_uid import token_to_uid
from channel_check import *



'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''


join = Blueprint('join', __name__)
@join.route('/channel/join', methods=['POST'])
def Join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_join(token, channel_id))

def channel_join(token, channel_id):

    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')

    if id_check(channel_id):
        raise ValueError(description = "Channel does not exist.")

    u_id = token_to_uid(token)

    global data
    data = getData()

    for i, items in data['channel_details'].items():
        if items['is_public'] == False:
            #Checking if channel is private
            for j, item in data['users'].items():
                if u_id == item['u_id']:
                #if permission is 3, does not have access
                    if item['permission'] == 3:
                    raise AccessError(description = "Channel is private, user is not an admin or owner of the slackr")


    # value error when channel does not exist

    for i, channel in data['channels'].items():
        print(channel)
        if channel['channel_id'] == int(channel_id):
            # get dictionary of users details
            for j, items in data['users'].items():
                if u_id == items['u_id']:
                    
                    ret = {}
                    ret['u_id'] = items['u_id']
                    ret['name_first'] = items['name_first']
                    ret['name_last'] = items['name_last']
                    data['channel_details'][int(channel_id)]['all_members'].append(ret)
                    return ret
            # if get to end of this loop, user isnt valid

    # if here channel doesnt exist                

