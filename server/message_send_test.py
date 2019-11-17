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
		
	with pytest.raises(ValueError, match = '*Invalid message*'):
		message_send(token1, channel_id, message)

#unauthorised user
def test_incorrect_user():
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	#user 1 sends a message to channel not apart of
	message = "A message you send"
	with pytest.raises(ValueError, match = '*Not an authorised user*'):
		message_send(user1_token, channel_id, message)

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