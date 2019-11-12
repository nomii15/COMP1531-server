from data import *

def channel_owner(channel_name, user_id):
    global data
    data = getData()

    #need to use channel_id instead of channel_name. wait for megan to add that in data structure
    for i, item in data['channel_details'].items():
        print(item)
        print(i)
        if item['name'] == channel_name:
            for dic in item['owner_members']:
                print("======")
                print(dic)
                if dic['u_id'] == user_id:
                    print("editor is an owner of the channel")
                    return True
    
    return False
