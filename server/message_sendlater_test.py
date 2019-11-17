from message_sendlater import message_sendlater
from channels_create import channels_create
from auth_register import auth_register
from datetime import datetime
from channel_join import channel_join
from data import *
import pytest

#test for invalid channel_id
def test_invalid_channel():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	user1_token = user['token']
		
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = int(channelResponse['channel_id'])
	
	channel_join(user1_token, channel_id)	

	message = "A valid message"

	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) + 100

	with pytest.raises(ValueError, match = '*Invalid Channel ID*'):
		message_sendlater(user1_token, channel_id + 1, message, time_sent)

#test for invalid message
def test_invalid_message():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	user1_token = user['token']
		
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = int(channelResponse['channel_id'])
	
	channel_join(user1_token, channel_id)	
	
	message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
	
	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) + 100
	
	with pytest.raises(ValueError, match = '*Invalid Message*'):
		message_sendlater(user1_token, channel_id, message, time_sent)

#test for invalid time
def test_invalid_time():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	user1_token = user['token']
		
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = int(channelResponse['channel_id'])

	channel_join(user1_token, channel_id)

	message = "A valid message"

	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) - 100

	with pytest.raises(ValueError, match = '*Invalid Time*'):
		message_sendlater(user1_token, channel_id, message, time_sent)
    
#valid cases
def test_valid():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
	user1_token = user['token']
		
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = int(channelResponse['channel_id'])

	channel_join(user1_token, channel_id)

	now = datetime.now()
	time_sent = int(datetime.timestamp(now)) + 100

	global Message
	expected_message_id = getMessage()

	message = "A valid message"
	message_sent = message_sendlater(user1_token, channel_id, message, time_sent)
	message_id = message_sent['message_id']

	assert message_id == expected_message_id