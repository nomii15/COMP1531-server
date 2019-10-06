'''
Make user with user id u_id an owner of this channel

ValueError when:
    Channel (based on ID) does not exist
    When user with user id u_id is already an owner of the channel

AccessError when:
    The authorised user is not an owner of the slackr, or an owner of this channel

'''

def channel_addowner(token, channel_id, u_id):
    pass