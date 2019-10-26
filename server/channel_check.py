from data import *
import jwt

#to check whether the authorised user is part of the given channel
def member_check(token, channel_id):

    global data    
    data = getData()
    global SECRET    
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id']

    for i,items in data['channel_details'].items():
        if u_id in items['all_members']:    
            return True
    return False
    
#check whether the given channel is valid
def id_check(channel_id):
    global data    
    data = getData()

    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            return True
        
    return False
