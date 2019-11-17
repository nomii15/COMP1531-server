from message_edit import message_edit
from auth_register import auth_register
from channels_create import channels_create
from channel_join import channel_join
from message_send import message_send
from data import *
import pytest

#test diff user tries to edit message
def test_incorrect_user():

	global data
	data = getData()

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
	new_message = 'user 2 wants to edit the message'
	
	#raise error if user 2 tries to edit
	with pytest.raises(ValueError, match = '*Not an authorised user*'):
		message_edit(user2_token , message_id , new_message)

#test owner tries to edit message
def test_owner_edit():

	global data
	data = getData()

	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	#user join that chanenl
	channel_join(user1_token, channel_id)
	
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']

	new_message = 'owner wants to edit the message'

	message_edit(owner_token, message_id, new_message)

	i = False
	for i, item in data['channels'].items():
		for currMessage in item['messages']:
			if currMessage['message_id'] == int(message_id) and currMessage['message'] == new_message:
				i = True
	
	assert i

#test message creator tries to edit own message
def test_user_edit():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	#user join that channel
	channel_join(user1_token, channel_id)
	
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']

	new_message = 'user wants to edit own message'

	message_edit(user1_token, message_id, new_message)

	i = False
	for i, item in data['channels'].items():
		for currMessage in item['messages']:
			if currMessage['message_id'] == int(message_id) and currMessage['message'] == new_message:
				i = True
	
	assert i

#test empty string in message edit (should remove the message)
def test_empty_string():

	global data
	data = getData()
	
	owner = auth_register("validemail1@gmail.com", "validpassword1", "OWNER1", "validname1")
	owner_token = owner['token']
	user1 = auth_register("validemail2@gmail.com", "validpassword1", "INCORRECT USER1", "validname2")
	user1_token = user1['token']
	
	#owner creates a channel
	channelResponse = channels_create(owner_token, "My Channel", True)
	channel_id = channelResponse['channel_id']
	
	#user join that channel
	channel_join(user1_token, channel_id)
	
	#user 1 sends a message
	message = "A message you send"
	message_sent = message_send(user1_token, channel_id, message)
	message_id = message_sent['message_id']

	new_message = ''

	message_edit(user1_token, message_id, new_message)

	i = False
	for i, item in data['channels'].items():
		for currMessage in item['messages']:
			if currMessage['message_id'] == int(message_id) and currMessage['message'] == new_message:
				i = True
	
	#shouldnt find the message with message_id in the data (i should remain False)
	assert i == False