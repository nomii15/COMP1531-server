from message_remove import message_remove
from auth_register import auth_register
from message_send import message_send
from channels_create import channels_create
from channel_join import channel_join
from data import *
import pytest

#test for message not found
def test_unknown_message():
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']

	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']

	message = "A message you send"
	message_send(owner_token, channel_id, message)
	#message_sent = message_send(owner_token, channel_id, message)
	#message_id = message_sent['message_id']

	with pytest.raises(ValueError, match = '*Invalid Message ID*'):
		message_remove(owner_token, -1)

#test for not authorised
def test_incorrect_user():
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	user2 = auth_register("validemail3@gmail.com", "validpassword1", "INCORRECT USER2", "validname3")
	user2_token = user2['token']
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	#two users join that chanenl
	channel_join(user2_token, channel_id)
	channel_join(user1_token, channel_id)
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	#raise error if user 2 tries to remove
	with pytest.raises(ValueError, match = '*Not an authorised user*'):
		message_remove(user2_token , message_id)

#user removes case
def test_user_removes():
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	#two users join that chanenl
	channel_join(user1_token, channel_id)
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	#raise error if user 2 tries to remove
	message_remove(user1_token, message_id)
	i = False
	for i,items in data['channels'].items():
		for item in items['messages']:
			if item['message_id'] == int(message_id):
				i = True
	#i should remain false - shouldnt find the message
	assert i == False

#owner removes case
def test_owner_removes():
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	#two users join that chanenl
	channel_join(user1_token, channel_id)
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']
	#raise error if user 2 tries to remove
	message_remove(owner_token, message_id)
	i = False
	for i,items in data['channels'].items():
		for item in items['messages']:
			if item['message_id'] == int(message_id):
				i = True
	#i should remain false - shouldnt find the message
	assert i == False