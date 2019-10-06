import pytest
from channel_leave import channel_leave
from auth_register import auth_register
from channels_list import channels_list

'''
Takes in token, channel_id // No return value

ValueError when:
Channel (based on ID) does not exist.

Given a channel ID, the user is removed as a member of this channel.
'''

def test_one():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_id1 = channels_create(token1, channel1, True)
    channel_leave(token1, channel1)
    channel_list1 = channels_list(token1)

    assert (channel_id1, channel1) not in channel_list1

def test_value_error():
    #setup
    register1 = auth_register("hello@gmail.com","abc","hi","hello")
    token1 = register1['token']

    #channel id does not exist
    with pytest.raises(ValueError,match=r"*"):
        channel_leave(token1,1)

