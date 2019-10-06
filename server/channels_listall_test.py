import pytest
from channels_listall import channels_listall
from auth_register import auth_register
from channels_create import channels_create

'''
Provide a list of all channels (and their associated details)

'''

def test_list_one():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("helloo@gmail.com","abcd","hihi","helloo")
    token2 = register2['token']
    u_id2 = register2['u_id']

    register3 = auth_register("hellooo@gmail.com","abcde","hihihi","hellooo")
    token3 = register3['token']
    u_id3 = register3['u_id']

    channel_id1 = channels_create(token1, channel1, True)
    channel_id2 = channels_create(token2, channel2, True)
    channel_id3 = channels_create(token3, channel3, True)
    
    channel_list1 = channels_listall(token1)

    #check all channels exist in the list
    assert (channel_id1, channel1) in channel_list1
    assert (channel_id2, channel2) in channel_list1
    assert (channel_id3, channel3) in channel_list1

def test_list_empty():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_list1 = channels_listall(token1)

    #check empty list as no channels have been created
    assert channel_list1 = []