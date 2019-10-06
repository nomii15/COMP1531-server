import pytest
from channel_join import channel_join
from auth_register import auth_register
from channel_join import channel_join
from channels_create import channels_create
from channels_list import channels_list

'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist

AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

def test_one():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("helloo@gmail.com","abcd","hihi","helloo")
    token2 = register2['token']
    u_id2 = register2['u_id']

    channel_id1 = channels_create(token1, channel1, True)
    channel_join(token2,channel_id)
    channel_list2 = channels_list(token2)

    assert (channel_id1, channel1) in channel_list2

def test_value_error():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']

    #channel id does not exist
    with pytest.raises(ValueError,match=r"*"):
        channel_join(token1,1)

def test_access_error():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    register2 = auth_register("helloo@gmail.com","abcd","hihi","helloo")
    token2 = register2['token']
    u_id2 = register2['u_id']

    channel_id1 = channels_create(token1, channel1, False)

    #channel is private
    with pytest.raises(AccessError,match=r"*"):
        channel_join(token2,channel_id1)