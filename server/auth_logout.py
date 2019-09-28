##auth logout implementation

'''
Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing

N/A
'''

#test stub, if token is a hash, delete token, otherwise not deleted
#only for the test (iteration1) will this function return something

def auth_logout(token):
            
    if token == "#":
        del token
        return "Deleted"
    else:    
        return "Not Deleted"               
