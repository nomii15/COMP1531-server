import pytest
from channel_leave import channel_leave
from auth_register import auth_register
from channels_list import channels_list
from data import *
from channels_create import channels_create

'''
Takes in token, channel_id // No return value

ValueError when:
Channel (based on ID) does not exist.

Given a channel ID, the user is removed as a member of this channel.
'''

def test_one():
    global data
    data = getData()
    #setup
    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    channel_id1 = channels_create(token1, 'channel1', True)
    channel_list1 = channels_list(token1)
    channel_leave(token1, channel_id1)
    channel_list2 = channels_list(token1)

    assert channel_list1 != channel_list2

def test_value_error():
    global data
    data = getData()
    #setup
    register2 = auth_register("validemail2@gmail.com", "validpassword2", "USER2", "validname2")
    token2 = register2['token']
    u_id2 = register2['u_id']

    #channel id does not exist
    with pytest.raises(ValueError,match=r"*"):
        channel_leave(token2,1)

