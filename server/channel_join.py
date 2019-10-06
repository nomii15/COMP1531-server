'''
Given a channel_id of a channel that the authorised user can join, adds them to that channel

ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

def channel_join(token, channel_id):
    pass