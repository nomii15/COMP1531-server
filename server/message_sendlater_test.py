from message_sendlater import *
import pytest

#test for invalid channel_id
def test_invalid_channel():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    time_sent = "2020-07-29 09:17:13.812189"
    with pytest.raises(ValueError, match = '*Invalid Channel ID*'):
        message_sendlater(token1, wrong_id, message, time_sent)

#test for invalid message
def test_invalid_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
    time_sent = "2020-07-29 09:17:13.812189"
    with pytest.raises(ValueError, match = '*The message you are trying to send is too large*'):
        message_sendlater(token1, channel_id, message, time_sent)

#test for invalid time
def test_invalid_time():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    time_sent = "2017-07-29 09:17:13.812189"
    with pytest.raises(ValueError, match = '*The time you selected is in the past*'):
        message_sendlater(token1, channel_id, message, time_sent)
    
#valid cases
def test_valid():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    time_sent = "2020-07-29 09:17:13.812189"
    
    assert (message_sendlater(token1, channel_id, message, time_sent) == {})