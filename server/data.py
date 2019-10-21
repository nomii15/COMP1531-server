# storing of lists for variables accross multiple functions

global SECRET
SECRET = 'COMP1531'

global user
user = 0

global channel
channel = 0

global data
data = {
    'users': {} 
    'channels' : {}
    'channel_details' : {}
    'messages' : {}
    'reacts': {}
}


def getData():
    global data
    return data

def getSecret():
    global SECRET
    return SECRET    

def getUsers():
    global user
    return user

def getChannels():
    global channel
    return channel

def incUser():
    global user
    user+=1        

def incChannel():
    global channel
    channel+=1 