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

    for i,items in data['channel_details'].items():
        #print(items['all_members'])
        for j in items['all_members']:
            #print(j)
            if u_id == j['u_id']:
                return True
    return False
    
#check whether the given channel is valid
def id_check(channel_id):
    global data    
    data = getData()

    for i,channel in data['channels'].items():
        if channel_id == i:
                return True
        
    return False
