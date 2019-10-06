'''
Given a users tokenID, send the message stored in the message parameter to the channel_id.

Value Errors-
    1. message being sent is greater than 1000 characters.
'''

def message_send(token, channel_id, message):
    if (len(message) > 1000):
        raise ValueError("Message too long")

    return {}