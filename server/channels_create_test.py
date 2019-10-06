import pytest
from channels_create import channels_create
from channels_list import channels_list
from auth_register import auth_register

'''
Creates a new channel with that name that is either a public or private channel

ValueError when:
    Name is more than 20 characters long

'''

def test_one():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_id1 = channels_create(token1, channel1, True)
    
    channel_list1 = channels_list(token1)

    #checks channel has been made
    assert (channel_id1, channel1) in channel_list1

def test_long_name():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']
    
    #name is more than 20 characters long
    with pytest.raises(ValueError,match=r"*"):
        channels_create(token1, thisisaverylongnamehehe, True)