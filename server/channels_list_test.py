import pytest
from channels_list import channels_list
from auth_register import auth_register
from channels_create import channels_create

'''
Provide a list of all channels (and their associated details) that the authorised user is part of

'''

def test_list_one():
    #setup
    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_id1 = channels_create(token1, 'channel1', True)
    
    channel_list1 = channels_list(token1)
    channel_list = {'channels': [{'channel_id': 1, 'name': 'channel1'}]}


    #check only channel user is part of exists in the list
    assert channel_list == channel_list1
    
def test_list_empty():
    #setup
    register2 = auth_register("validemail2@gmail.com", "validpassword2", "USER2", "validname2")
    token2 = register2['token']
    u_id2 = register2['u_id']

    register3 = auth_register("validemail3@gmail.com", "validpassword3", "USER3", "validname3")
    token3 = register3['token']
    u_id3 = register3['u_id']

    register4 = auth_register("validemail4@gmail.com", "validpassword4", "USER4", "validname4")
    token4 = register4['token']
    u_id4 = register4['u_id']

    channel_id2 = channels_create(token2, 'channel2', True)
    channel_id3 = channels_create(token3, 'channel3', True)
    
    channel_list4 = channels_list(token4)
    empty_list = {'channels' : []}

    #check channel list is empty as user does not belong to any channels
    assert channel_list4 == empty_list