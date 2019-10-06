from message_remove import *
import pytest

#test for message not found
def test_unknown_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A message you send"
    message1 = "A message you dont send"
    message_send(token1, channel_id, message)
    with pytest.raises(ValueError, match = '*Message could not be found*'):
        message_remove(token1, message1)

#test for message not found
def test_incorrect_user():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    u_id2, token2 = auth_register("validemail1@gmail.com", "validpassword1", "ADMIN", "validname")
    u_id3, token3 = auth_register("validemail1@gmail.com", "validpassword1", "OWNER", "validname")
    u_id4, token4 = auth_register("validemail1@gmail.com", "validpassword1", "INCORRECT USER", "validname")
    #owner creates a channel
    channelResponse = channels_create(token3, "My Channel", True)
    channel_id = channelResponse['channel_id']
    #two users join that chanenl
    channel_join(token1, channel_id)
    channel_join(token4, channel_id)
    #user 1 sends a message
    message = "A message you send"
    message_send(token1, channel_id, message)
    #raise error if user 4 tries to edit that message
    with pytest.raises(ValueError, match = '*Not an authorised user*'):
        message_remove(token4, message)



#Valid
def test_vaild():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A message you send"
    message_send(token1, channel_id, message)

    assert (message_remove(token1, message) == {})
