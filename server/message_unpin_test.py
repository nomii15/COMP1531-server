from message_unpin import *
import pytest

#You would never reach access error because you only ever search for channels in which the user is apart of

#test for invalid message
def test_invalid_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message_valid = "Hello this is valid"
    messaage_invalid = "this is invalid"
    with pytest.raises(ValueError, match = '*Invalid messageId*'):
        message_unpin(token1, message_invalid)

#test for user not admin
def test_authorisation():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    u_id2, token2 = auth_register("validemail1@gmail.com", "validpassword1", "ADMIN", "validname")
    channelResponse = channels_create(token2, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message_valid = "A valid message"
    with pytest.raises(ValueError, match = '*User is not an admin*'):
        message_unpin(token1, message_valid)
    
#valid cases
def test_valid():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    
    assert (message_unpin(token1, message) == {})