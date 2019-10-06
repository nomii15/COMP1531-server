from message_react import *
import pytest

#test for message not found
def test_invalid_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    #owner creates a channel
    channelResponse = channels_create(token1, "My Channel", True)
    channel_id = channelResponse['channel_id']
    #user 1 sends a message
    message = "A message you send"
    message1 = "An invalid message"
    message_send(token1, channel_id, message)

    with pytest.raises(ValueError, match = '*Invalid messageId*'):
        message_react(token1, message1, 1)

#test for invalid react
def test_invalid_react():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    #owner creates a channel
    channelResponse = channels_create(token1, "My Channel", True)
    channel_id = channelResponse['channel_id']
    #user 1 sends a message
    message = "A message you send"
    message_send(token1, channel_id, message)

    with pytest.raises(ValueError, match = '*Invalid react id*'):
        message_react(token1, message, -1)

#test for message already reacted
def test_message_reacted():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    #owner creates a channel
    channelResponse = channels_create(token1, "My Channel", True)
    channel_id = channelResponse['channel_id']
    #user 1 sends a message
    message = "A message you send"
    message_send(token1, channel_id, message)
    message_react(token1, message, 1)

    with pytest.raises(ValueError, match = '*Invalid React Id*'):
        message_unreact(token1, message, 1)

#Valid
def test_vaild():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "USER", "validname")
    #owner creates a channel
    channelResponse = channels_create(token3, "My Channel", True)
    channel_id = channelResponse['channel_id']
    #user 1 sends a message
    message = "A message you send"
    message_send(token1, channel_id, message)

    assert (message_react(token1, message, 1) == {})