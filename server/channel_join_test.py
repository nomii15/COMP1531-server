import pytest
from channel_join import channel_join
from auth_register import auth_register
from channel_join import channel_join
from channels_create import channels_create
from channels_list import channels_list

from data import *

'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist

AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

def test_one():
    global data
    data = getData()
    #setup
    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("validemail2@gmail.com", "validpassword2", "USER2", "validname2")
    token2 = register2['token']
    u_id2 = register2['u_id']

    channel_id1 = channels_create(token1, 'channel1', True)
    channel_join(token2, channel_id1)
    channel_list1 = channels_list(token1)
    print(channel_list1)
    channel_list2 = channels_list(token2)
    channel_list = {'channels': [{'channel_id': 1, 'name': 'channel1'}]}
    assert channel_list == channel_list2

def test_value_error():
    global data
    data = getData()
    #setup
    register3 = auth_register("validemail3@gmail.com", "validpassword3", "USER3", "validname3")
    token3 = register3['token']
    u_id3 = register3['u_id']

    #channel id does not exist
    with pytest.raises(ValueError,match=r"*"):
        channel_join(token3,1)

def test_access_error():
    global data
    data = getData()
    #setup
    register4 = auth_register("validemail4@gmail.com", "validpassword4", "USER4", "validname4")
    token4 = register4['token']
    u_id4 = register4['u_id']

    register5 = auth_register("validemail5@gmail.com", "validpassword5", "USER5", "validname5")
    token5 = register5['token']
    u_id5 = register5['u_id']

    channel_id4 = channels_create(token4, 'channel4', False)

    #channel is private
    with pytest.raises(AccessError,match=r"*"):
        channel_join(token5,channel_id4)