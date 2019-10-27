#definition channels_list function
from flask import Flask, request, Blueprint
from json import dumps
from Error import AccessError
import hashlib
import jwt

# importing the data file
from data import *

import pytest
from channels_create import channels_create
from channels_list import channels_list
from auth_register import auth_register
from email_check import email_check

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''

class testCreate():
    def __init__(self, token, name, is_public):
        self.token = token
        self.name = name
        self.is_public = is_public

    def nameTest(self):
        if len(name) > 20:
            raise ValueError("Channel name too long")

    def setup(self):
        global data
        data = getData()

        global channel
        channel = getChannels()

        channel_id = channel

        data['channels'][channel] = {'channel_id': channel_id, 'name': self.name, 'messages': []}

        # retrieve u_id from token
        global SECRET 
        SECRET = getSecret()

        token_payload = jwt.decode(self.token, SECRET, algorithms=['HS256'])
        u_id = token_payload['u_id']

        detail = {}
        for i, items in data['users'].items():
            if items['u_id'] == u_id:
                detail['u_id'] = items['u_id']
                detail['name_first'] = items['name_first']
                detail['name_last'] = items['name_last']
                break

        # adding to channel details, registering as a member of the channel
    
        data['channel_details'][channel] = {'name' : self.name, 'owner_members' : [], 'all_members' : [] , 'public': self.is_public}
        data['channel_details'][channel]['owner_members'].append(detail)
        data['channel_details'][channel]['all_members'].append(detail)
        incChannel()
        #print(data['channel_details'])

        return channel_id

def test_one():
    register1 = setup_register()
    token1 = register1['token']
    u_id1 = register1['u_id']

    test = testCreate(token1, 'channel1', True)

    channel_id1 = test.setup()
    
    channel_list1 = setup_list(token1)#['channel_id']

    #checks channel has been made
    assert ({'channel_id':0,'name':channel1}) in channel_list1['channels']
    #assert ('name': 'channel1') in channel_list1

def test_long_name():
    #setup
    register1 = setup_register()
    token1 = register1['token']
    u_id1 = register1['u_id']

    #name is more than 20 characters long
    with pytest.raises(ValueError,match=r"*"):
        
        test = testCreate(token1, thisisaverylongnamehehe, True)
        test.nameTest()

def setup_register():

    email = 'hello@gmail.com'
    password = 'abcdef'
    name_first = 'hi'
    name_last = 'hello'

    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")

    #password length check
    if len(password) < 5:
        raise ValueError("Invalid Password Length")
        
    #first name length check    
    if len(name_first) > 50 or len(name_first) == 0:
        raise ValueError("Invalid First Name Length")
    
    #last name length check   
    if len(name_last) > 50 or len(name_last) == 0:
        raise ValueError("Invalid Last Name Length")


    # add user dictionary to add to the global dictionary

    # create new user to the data dictionary, need to check syntax
    global data
    data = getData()

    # check to see if the email is already registered
    for em,pas in data['users'].items():
        if pas['email'] == email:
            raise ValueError("Email already exists")

    # if it gets here, its a valid user
    global user
    user = getUsers()


    handle = name_first.lower() + name_last.lower()
    handle = ''.join(handle)

    # if the u_id is greater than 20 character, reduce
    if len(handle)>17:
        handle = handle[0:17]

    # also add number to reduce handle conflicts
    handle = handle + str(user)
    handle = ''.join(handle)

    if len(handle) > 20:
        handle = handle[0:19]

    u_id = user

    data['users'][user] = {'email': email, 'password': hashlib.sha256(password.encode()), 'name_first': name_first,
     'name_last': name_last, 'u_id': u_id, 'loggedin': True, 'handle': handle}
    incUser()

    global SECRET
    SECRET = getSecret()

    #ret['u_id'] = u_id
    token = jwt.encode({'u_id':u_id}, SECRET, algorithm='HS256').decode('utf-8')
    ret  = dict()
    ret['u_id'] = u_id
    ret['token'] = token
  
    #print(ret)
    return ret

def setup_list(token):

    global data
    data = getData()

    #extract u_id from token
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']

    channelret = []

    #for each channel, check if user is a member
    for i,channel in data['channel_details'].items():
        #print(channel)
        for j in channel['all_members']:
            if j['u_id'] == u_id:
                channelret.append({'channel_id': i, 'name': channel['name']})

    ret = {'channels': channelret} 
    #print(ret)       
    '''
    ret = dict()
    for channel in channel_list:
        del channel['channel'][channel]['messages']
        ret['channel'] = data['channel'][channel]#[['name']['channel_id']] <= check how to only return these two fields 
    '''
    return ret