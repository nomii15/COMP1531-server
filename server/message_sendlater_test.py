from message_sendlater import message_sendlater
from channels_create import channels_create
from auth_register import auth_register
from datetime import datetime
from data import *
import pytest

#test for invalid channel_id
def test_invalid_channel():
    user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    token1 = user['token']

    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = int(channelResponse['channel_id']) + 1

    message = "A valid message"
	
	now = datetime.now()
    time_sent = int(datetime.timestamp(now)) + 100

    with pytest.raises(ValueError, match = '*Invalid Channel ID*'):
        message_sendlater(token1, channel_id, message, time_sent)

#test for invalid message
def test_invalid_message():
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	token1 = user['token']
	
	channelResponse = channels_create(token1, "My Channel", False)
	channel_id = int(channelResponse['channel_id'])
	
	message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
	
	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) + 100
	
	with pytest.raises(ValueError, match = '*The message you are trying to send is too large*'):
		message_sendlater(token1, channel_id, message, time_sent)

#test for invalid time
def test_invalid_time():
    user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    token1 = user['token']

    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = int(channelResponse['channel_id'])

    message = "A valid message"

	now = datetime.now()
    time_sent = int(datetime.timestamp(now)) - 100

    with pytest.raises(ValueError, match = '*The time you selected is in the past*'):
        message_sendlater(token1, channel_id, message, time_sent)
    
#valid cases
def test_valid():
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	token1 = user['token']

	channelResponse = channels_create(token1, "My Channel", False)
	channel_id = int(channelResponse['channel_id'])

	message = "A valid message"

	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) + 100
		
	global Message
	message_id = getMessage()

	assert (message_sendlater(token1, channel_id, message, time_sent) == {'message_id': message_id})