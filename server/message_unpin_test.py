from message_unpin import message_unpin
from message_pin import message_pin
from auth_register import auth_register
from channels_create import channels_create
from channel_join import channel_join
from message_send import message_send
from data import *
import pytest

#test for invalid message
def test_invalid_message():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	#owner sends a message
	message = "A message you send"
	message_sent = message_send(owner_token, channel_id, message)
	message_id = message_sent['message_id']
	
	#raise error if wanting to pin invalid message
	message_pin(owner_token , message_id)
	with pytest.raises(ValueError, match = '*Invalid Message ID*'):
		message_unpin(owner_token , -1)

#test for user not admin
def test_authorisation():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	channel_join(user1_token, channel_id)
	
	#owner sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	
	#raise error if wanting to pin invalid message
	message_pin(owner_token , message_id)
	with pytest.raises(ValueError, match = '*Not an authorised user*'):
		message_unpin(user1_token , message_id)
		
#test already pinned
def test_unpinned():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	channel_join(user1_token, channel_id)
	
	#owner sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	
	#raise error if wanting to pin invalid message
	with pytest.raises(ValueError, match = '*Message already unpinned*'):
		message_unpin(owner_token , message_id)

#valid cases
def test_valid():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	channel_join(user1_token, channel_id)
	
	#owner sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	
	#raise error if wanting to pin invalid message
	message_pin(owner_token, message_id)
	message_unpin(owner_token, message_id)
	unpinned = False
	for i, items in data['channels'].items():
		for item in items['messages']:
			if item['message_id'] == int(message_id) and item['is_pinned'] == False:
				unpinned = True

	assert unpinned == True
