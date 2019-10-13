##auth logout implementation

'''
Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing

N/A
'''


def auth_logout(token):

    # create the dictionary
    ret = {}
    # if the token is a valid token, delete the token and return true
    # otherwise, return false
    if token == valid_token:
        del(token)
        ret['is_success'] = True
    else:
        ret['is_success'] = False

    # return the dictionary
    return ret    


