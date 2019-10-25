from data import *

#to check whether the authorised user is part of the given channel
def member_check(token, channel_id):

    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id']
    
    for member in data['channel_details']['channel_id']['all_members']:
        if u_id == member:
            return True
    
    return False
    
    
#check whether the given channel is valid
def id_check(channel_id):
    for channel in data['channels']:
        if channel['channel_id'] == channel_id
        return True
        
    return False
