import pytest
from channel_addowner import channel_addowner
from auth_register import auth_register
from channels_create import channels_create
from data import *

'''
Make user with user id u_id an owner of this channel

ValueError when:
    Channel (based on ID) does not exist
    When user with user id u_id is already an owner of the channel

AccessError when:
    The authorised user is not an owner of the slackr, or an owner of this channel

'''

def test_value_error_channel():
    global data
    data = getData()

    register1 = auth_register("validemail1@gmail.com", "validpassword1", "USER1", "validname1")
    token1 = register1['token']
    u_id1 = register1['u_id']

    #channel id does not exist
    with pytest.raises(ValueError,match=r"*"):
        channel_addowner(token1,1,u_id1)

def test_value_error_owner():
    global data
    data = getData()
    #print(data)
    register2 = auth_register("validemail2@gmail.com", "validpassword2", "USER2", "validname2")
    token2 = register2['token']
    u_id2 = register2['u_id']

    channel_id2 = channels_create(token2, 'channel1', True)

    #user is already an owner of the channel
    with pytest.raises(ValueError,match=r"*"):
        channel_addowner(token2,channel_id2,u_id2)

def test_access_error():
    global data
    data = getData()
    register3 = auth_register("validemail3@gmail.com", "validpassword3", "USER3", "validname3")
    token3 = register3['token']
    u_id3 = register3['u_id']

    register4 = auth_register("validemail4@gmail.com", "validpassword4", "USER4", "validname4")
    token4 = register4['token']
    u_id4 = register4['u_id']

    channel_id4 = channels_create(token4, 'channel4', True)

    #authorised user is not owner of slackr or channel
    with pytest.raises(ValueError,match=r"*"):
        channel_addowner(token4, channel_id4, u_id3)