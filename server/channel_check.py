from data import *
import jwt

#to check whether the authorised user is part of the given channel
def member_check(token, channel_id):

    global data    
    data = getData()
    global SECRET    
    SECRET = getSecret()

    Payload = jwt.decode(token, SECRET, algorithms='HS256')
    u_id = Payload['u_id']

    for items in data['channel_details'].items():
        if u_id in items['all_members']:    
            return True
    return False
    
#check whether the given channel is valid
def id_check(channel_id):
    global data    
    data = getData()

    for Channel in data['channels'].items():
        if channel_id == Channel['channel_id']:
                return True
        
    return False
