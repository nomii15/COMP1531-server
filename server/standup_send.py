#definition of the standup_send function

'''
Sending a message to get buffered in the standup queue, assuming a standup is currently active

ValueError when:
Channel (based on ID) does not exist
Message is more than 1000 characters

AccessError when
The authorised user is not a member of the channel that the message is within
If the standup time has stopped
'''

def standup_send(token, channel_id, message):
    pass
