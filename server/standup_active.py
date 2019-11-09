from data import *
from flask import Flask, request, Blueprint
from json import dumps
from token_check import token_check
from channel_check import id_check

def standup_active(token, channel_id):
    if token_check(token) == "Invalid_token":
        raise ValueError("Invalid Token")

    # check channel id
    if id_check(channel_id)==False:
        raise ValueError("Invalid Channel ID")

    # by default, is active is false and time finish is none when 
    # channel is created, only when standup start is 
    # called when these variables change
    global data 
    data = getData()

    global standup
    standup = getStandup()

    # get the current time 
    dt = datetime.utcnow()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    if timestamp > data['channels'][channel_id]['time_finish']:
        #need to send the data from standup to the channel
        stand_message = ""
        for i in standup.items():
            if i['channe_id'] == channel_id:
                for j in i['messages']:
                    #get the user and the message they sent
                    stand_message = stand_message + j['name'] + ": " + j['message'] + "\n"
                standup.remove(i) 
                # have all the messages, delete standup and send message as person who started standup
                message_send()


    return {    
        'is_active': data['channels'][channel_id]['standup_active'],
        'time_finish': data['channels'][channel_id]['time_finish']    
    }


active = Blueprint('active', __name__)

@active.route('/standup/active', methods=['GET'])
def route():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))
    #print(token, channel_id)
    return dumps( standup_active(token, channel_id) )
