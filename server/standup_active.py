from data import *
from flask import Flask, request, Blueprint
from json import dumps
from token_check import token_check
from channel_check import id_check
from datetime import datetime, timezone
from message_send import message_send
from channel_messages import channel_messages
import calendar


def standup_active(token, channel_id):
    if token_check(token) == False:
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
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    #print (unixtime)

    if data['channels'][channel_id]['time_finish'] == None:
        return {    
        'is_active': data['channels'][channel_id]['standup_active'],
        'time_finish': data['channels'][channel_id]['time_finish']    
        }  

    if unixtime >= data['channels'][channel_id]['time_finish']:
        #need to send the data from standup to the channel
        stand_message = ""
        for i in standup:
            if i['channel_id'] == channel_id:
                for j in i['messages']:
                    #get the user and the message they sent
                    stand_message = stand_message + j['name'] + ": " + j['message'] + "\n"
                standup.remove(i) 
                # have all the messages, delete standup and send message as person who started standup
                print(stand_message)
                message_send(token, channel_id, stand_message)
                ##channel_messages(token, channel_id, 0)

                #reset standup variables and return
                data['channels'][channel_id]['standup_active'] = False
                data['channels'][channel_id]['time_finish'] = None
                return {    
                    'is_active': data['channels'][channel_id]['standup_active'],
                    'time_finish': data['channels'][channel_id]['time_finish']    
                }
    else:            
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
