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

def test_one():
    #setup
    global data
    data = getData()

    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_id1 = channels_create(token1, 'channel1', True)
    channel_list1 = channels_list(token1)
    channel_list = {'channels': [{'channel_id': 1, 'name': 'channel1'}]}

    #checks channel has been made
    assert channel_list == channel_list1

def test_long_name():    
    register2 = auth_register("validemail2@gmail.com", "validpassword2", "USER2", "validname2")
    token2 = register2['token']
    u_id2 = register2['u_id']
    #name is more than 20 characters long
    with pytest.raises(ValueError,match=r"*"):
        channels_create(token2, 'thisisaverylongnamehehe', True)
