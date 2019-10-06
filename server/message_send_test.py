from message_send import *
import pytest

#test for invalid message
def test_long_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
    with pytest.raises(ValueError, match = '*Message too long*'):
        message_send(token1, channel_id, message)

#valid cases
def test_valid_case():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    
    assert (message_send(token1, channel_id, message) == {})