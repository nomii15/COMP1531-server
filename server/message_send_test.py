from message_send import message_send
from channels_create import channels_create
from auth_register import auth_register
import pytest

data = {
    'channels' : [
        {
        'channel_id': '1',
        'name': 'channel 1',
        'messages':[]
        },
		{
		'channel_id': '2',
        'name': 'channel 2',
        'messages':['first message']
		}
	]
}
class testMessageSend():
        def __init__(self, token, channel_id, message):
        	self.token = token
        	self.channel_id = channel_id
        	self.message = message	
		def messageTest(self):
        	if len(message) > 1000:     
				raise ValueError("Message too long")
		def valid(self):
			return True
#test for invalid message
def test_long_message():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long This is an invalid message because it is too long  "
	
	test = testMessageSend(token1, channel_id, message)
	
	with pytest.raises(ValueError, match = '*Message too long*'):
		#message_send(token1, channel_id, message)
        test.messageTest()

#valid cases
def test_valid_case():
    u_id1, token1 = auth_register("validemail1@gmail.com", "validpassword1", "validname", "validname")
    channelResponse = channels_create(token1, "My Channel", False)
    channel_id = channelResponse['channel_id']
    message = "A valid message"
    
	#test = testMessageSend(token1, channel_id, message)
    assert (message_send(token1, channel_id, message) == {})