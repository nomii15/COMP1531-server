'''
Given a users tokenID, send the message stored in the message parameter to the channel_id at the specified time

Value Errors-
    1. channel_id does not exist
    2. message being sent is greater than 1000 characters.
    3. time_sent is in the past

Access Errors-
    1. not subscribed to channel_id
'''
from datetime import datetime

def message_sendlater(token, channel_id, message, time_sent):
    subscribedChannels = channels_list(token)
    if channel_id not in subscribedChannels:
        raise ValueError("Invalid Channel ID")

    if len(message) > 1000:
        raise ValueError("The message you are trying to send is too large")
    
    if time_sent < datetime.now().time():
        raise ValueError("The time you selected is in the past")

    return {}