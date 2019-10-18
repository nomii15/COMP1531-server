from flask import Flask, request
from json import dumps
import jwt
import hashlib


APP = Flask(__name__)

# global list of dictionaries for messages
messages = [

]

def getM():
    global messages
    return messages


@APP.route('/channel/messages', methods = ['GET'])
def getMessages():

    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')

    if not a member of the channel:
        raise AccessError("Not a member")

    message = {
        'messages': {},
        'start': start,
        'end': , 
    }

    for channel in channel['id']:
        if channel == channel_id:
            # get the messages
            # add to message return

            #check if valid start point to read messages
            if start >= len(message['messages']:
                raise ValueError("Start greater than number of messages")

            if len(message['messages']) < 50:
                message['end'] = -1
            else:    
                message['end'] = start+50
            

        else
            pass    


    return dumps(messages)
    


    # check that the channel id is correct

    # check valid token

    # get the messages from the channel id
    