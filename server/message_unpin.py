'''
Given a users tokenID and a message Id, unpin the message

Value Errors-
    1. message_id not a valid message
    2. authorised user is not an admin
    3. message not pinned
AccessError-
    1. Authorised user is not a memeber of channel
'''

def message_unpin(token,message_id):

    #all channels user is apart of
    all_channels = channels_list(token)
    #number of channels user is apart of
    number_of_channels = len(all_channels)
    n = 0
    for channel in all_channels:
        #increment to keep track of number of searched channels
        n += 1
        #for each channel get the channel id
        variable_channel_id = channel.get("id")
        #for each channel id get the channel details
        variable_channel_details = channel_details(token, variable_channel_id)
        #extract the list of dictionaries of channel owners for the specified channel
        variable_channel_owners = variable_channel_details.get("owner_members")
        #initialise channel messages and a variable i
        i = 0
        variable_all_messages_dict = {'end': 0}
        #while you havent reached the end of the channel messages
        while variable_all_messages_dict.get("end") != -1:
            #extract the first 50 channel messages, start index and end index
            variable_all_messages_dict = channel_messages(token, variable_channel_id, i)
            i += 50
            #extract just the messages dictionary without the start/end index
            varirable_all_messages = variable_all_messages_dict.get("messages")
            #find the target message you want to edit in
            target_message = next((item) for item in variable_all_messages if item["message_id"] == message_id, '-1')
            #if could not find target message continue to next iter in loop
            if target_message == '-1':
                continue
            else:
                #if user is not an admin error/break
                if target_message.get('u_id') not in variable_channel_owners:
                    raise ValueError("User is not an admin")
                #elif message is not pinned error/break
                #else implement the unpin message here - MAKE SURE TO DECREMENT N ONCE, THEN BREAK FROM ALL LOOPS
                pass

    #if all the channels have been searched, this means no message has been found
    #need to decrement n once in implementation to not accidently call error in the case the message is found in the last channel search
    if n == number_of_channels:
        raise ValueError("Invalid messageId")

    return {}