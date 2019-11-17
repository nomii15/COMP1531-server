import pytest
from channels_listall import channels_listall
from auth_register import auth_register
from channels_create import channels_create

'''
Provide a list of all channels (and their associated details)

'''
def test_list_empty():
    #setup
    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_list1 = channels_listall(token1)
    empty_list = {'channels' : []}

    #check empty list as no channels have been created
    assert channel_list1 == empty_list

def test_list_one():
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
    channel_id4 = channels_create(token4, 'channel4', True)

    channel_listall2 = channels_listall(token2)
    channel_listall3 = channels_listall(token3)
    channel_listall4 = channels_listall(token4)
    channel_list = {'channels': [{'name': 'channel2', 'channel_id': 1}, {'name': 'channel3', 'channel_id': 2}, {'name': 'channel4', 'channel_id': 3}]}

    #check all channels exist in the list
    assert channel_listall2 == channel_list
    assert channel_listall3 == channel_list
    assert channel_listall4 == channel_list