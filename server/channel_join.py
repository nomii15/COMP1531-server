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

    #Access error if token is invalid
    if token_check(token) == False:
        raise AccessError(description = 'Invalid Token')

    #Value error if channel does not exist
    if id_check(channel_id):
        raise ValueError(description = "Channel does not exist.")

    u_id = token_to_uid(token)

    global data
    data = getData()

    for j, item in data['users'].items():
        if u_id == item['u_id']:
            #Checking user slackr permissions
            if item['permission'] == 3:
                #If user is a member and channel is private - no access
                for i, items in data['channel_details'].items():
                    if items['is_public'] == False:
                        #Checking if channel is private
                        raise AccessError(description = "Channel is private, user is not an admin or owner of the slackr")
                is_admin = False
            else:
                is_admin = True 

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
                    #If user is an admin of the slackr, setting as owner member of channel
                    if is_admin == True:
                        data['channel_details'][int(channel_id)]['owner_members'].append(ret)
                    return {}
