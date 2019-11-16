from message_send import message_send
from channels_create import channels_create
from auth_register import auth_register
from data import *
import pytest

#test for invalid message
def test_long_message():
    user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    token1 = user['token']
        
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = int(channelResponse['channel_id'])
        
    message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
        
    with pytest.raises(ValueError, match = '*Meessage too long*'):
        message_send(token1, channel_id, message)

#valid cases
def test_valid_case():
    user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    token1 = user['token']
        
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = int(channelResponse['channel_id'])
        
    message = 'A valid message'	
    global Message
    message_id = getMessage()

    assert (message_send(token1, channel_id, message) == {'message_id': message_id})