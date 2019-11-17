from message_react import message_react
from auth_register import auth_register
from channels_create import channels_create
from channel_join import channel_join
from message_send import message_send
from data import *
import pytest

#test for message not found
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
	message_send(owner_token, channel_id, message)
	
	#raise error if wanting to pin invalid message
	with pytest.raises(ValueError, match = '*Invalid Message ID*'):
		message_react(owner_token , -1, 1)

#test for invalid react
def test_invalid_react():

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
	with pytest.raises(ValueError, match = '*Invalid React ID*'):
		message_react(user1_token , message_id, 2)


#test for message already reacted
def test_message_reacted():

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
	message_react(user1_token, message_id, 1)
	
	#raise error if wanting to pin invalid message
	with pytest.raises(ValueError, match = '*Already reacted*'):
		message_react(user1_token , message_id, 1)

#Valid
def test_vaild():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	user1_uid = user1['u_id']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	channel_join(user1_token, channel_id)

	#owner sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	message_react(user1_token, message_id, 1)

	reacted = False
	for i,items in data['channels'].items():
		for item in items['messages']:
			if item['message_id'] == int(message_id):
				for react in item['reacts']:
					if react['react_id'] == 1:
						if user1_uid in react['u_ids']:
							reacted = True

	assert reacted == True