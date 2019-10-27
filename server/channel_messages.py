from flask import Flask, request, Blueprint
from json import dumps
import jwt
import hashlib

from Error import *
from token_check import *
from channel_check import *
from data import *


channel_message = Blueprint('channel_message', __name__)

@channel_message.route('/channel/messages', methods = ['GET'])
def getMessages():

    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))
    start = int(request.args.get('start'))


    global data
    data = getData()

    if token_check(token) == False:
        raise ValueError("Invalid token")

    if member_check(token, channel_id) == False:
        AccessError("Not a member")

    # return dictionary of the messages found, with initialisation
    message = {
        'messages': [],
        'start': start,
        'end': 0, 
    }

    for i,channel in data['channels'].items():
        #print(channel['channel_id'])
        #print(channel_id)
        if channel_id == channel['channel_id']:
            # get the messages
            # add to message return
            if len(data['channels'][channel_id]['messages']) == 0:
                return dumps(message)
            
            #check if valid start point to read messages
            if start >= len( data['channels'][channel_id]['messages'] ):
                raise ValueError("Start greater than number of messages")

            if len(message['messages']) < 50:
                message['end'] = -1
            else:    
                message['end'] = start+50

            for i in range(start, end):
                message['messages'].append(data['channels'][channel_id]['messages'][i] )  

            #print(message)              
            return dumps(message)

        else:
            pass


    # no match for a channel
    raise ValueError("No channel matches the channel id given")


    # check that the channel id is correct

    # check valid token

    # get the messages from the channel id
    