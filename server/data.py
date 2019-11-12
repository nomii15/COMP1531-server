# storing of lists for variables accross multiple functions
from werkzeug.exceptions import HTTPException

global SECRET
SECRET = 'COMP1531'

global user
user = 1

global channel
channel = 1

global Message
Message = 1

global data
data = {
    'users': {},
    'channels' : {},
    'channel_details' : {}
}

# temp standup buffer to hold message during that time
global standup
standup = []

def getStandup():
    global standup
    return standup

global reset
reset = {
    'codes': {}
}

def getData():
    global data
    return data

def getMessage():
    global Message
    return Message 

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

def incMessage():
    global Message
    Message+=1    

def getReset():
    global reset
    return reset

# error handling
class ValueError(HTTPException):
    code = 400
    message = 'No message specified'
