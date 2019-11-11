#implementation of function standup_start
from data import *
from flask import Flask, request, Blueprint
from json import dumps
from token_check import token_check
from channel_check import id_check, member_check
from Error import AccessError
from datetime import timezone, datetime
import jwt

'''
For a given channel, start the standup period whereby for the next 15 minutes if someone calls "standup_send" with a message, it is buffered during the 15 minute window then at the end of the 15 minute window a message will be added to the message queue in the channel from the user who started the standup.

ValueError when:Channel (based on ID) does not exist
AccessError whenThe authorised user is not a member of the channel that the message is within
'''

def standup_start(token, channel_id, length):
    
    #check token
    if token_check(token) == "Invalid_token":
        raise ValueError("Invalid Token")

    # check channel id
    if id_check(channel_id)==False:
        raise ValueError("Invalid Channel ID")

    #check if member of channel
    if member_check(token, channel_id) == False:
        raise AccessError("Not a member of the channel")
    
    global data 
    data = getData()    

    # check whether a standup is already active
    if data['channels'][channel_id]['standup_active'] == True:
        raise ValueError("Standup already active")

    # get the current time
    dt = datetime.utcnow()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    #print(timestamp) 

    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']  

    # change the stantup variable to true and input the time
    data['channels'][channel_id]['standup_active'] = True
    data['channels'][channel_id]['startup_user'] = u_id
    data['channels'][channel_id]['time_finish'] = timestamp + length
    return data['channels'][channel_id]['time_finish']



start = Blueprint('start', __name__)
@start.route('/standup/start', methods=['POST'])
def start_route():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    length = int(request.form.get('length'))
    return dumps( standup_start(token, channel_id, length)  )

