from flask import Flask, request, Blueprint
from json import dumps
import jwt
import hashlib

from Error import *
from token_check import *
from channel_check import *
from data import *


def channel_messages(token, channel_id, start):

    global data
    data = getData()

    if token_check(token) == False:
        raise ValueError(description = "Invalid token")

    if member_check(token, channel_id) == False:
        raise AccessError(description = "Not a member")

    # return dictionary of the messages found, with initialisation
    message = {
        'messages': [],
        'start': start,
        'end': 0, 
    }

    for i,channel in data['channels'].items():
        #print(channel['channel_id'])
        #print(channel)
        if int(channel_id) == channel['channel_id']:
            # get the messages
            # add to message return

            if data['channels'][channel_id]['messages'] == None:
                return message
            
            #check if valid start point to read messages
            if start > len(data['channels'][channel_id]['messages']):
                raise ValueError(description = "Start greater than number of messages")

            if len(data['channels'][channel_id]['messages']) > 50 and start==0:
                message['end'] = 49
                end = len(data['channels'][channel_id]['messages'])

            elif (len(data['channels'][channel_id]['messages']) - start) < 50:    
                message['end'] = -1
                end = -1
                #end = len(data['channels'][channel_id]['messages'])
            
            for items in data['channels'][channel_id]['messages']:
                message['messages'].append(items)
                
            ## range is wrong 
            #for i in range(start, end):
            #    items = data['channels'][channel_id]['messages']
            #    #print(items)
            #    for j in items:
            #        print(j)
            #        message['messages'].append(j['message'] ) 
            

            for i in range(start, end):
                message['messages'].append(data['channels'][channel_id]['messages'][i] )  

            #print(message)              
            return message

        else:
            pass


    # no match for a channel
    raise ValueError(description = "No channel matches the channel id given")


    # check that the channel id is correct

    # check valid token

    # get the messages from the channel id





channel_message = Blueprint('channel_message', __name__)

@channel_message.route('/channel/messages', methods = ['GET'])
def getMessages():

    token = str(request.args.get('token'))
    channel_id = int(request.args.get('channel_id'))
    start = int(request.args.get('start'))
    return dumps( channel_messages(token, channel_id, start)     )
