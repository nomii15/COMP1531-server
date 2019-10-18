# check to see if a valid token
from data import *
import jwt

def token_check(token, u_id):
    
    
    global SECRET
    SECRET = getSecret()

    global data
    data = getData()

    test = jwt.decode(token, SECRET, algorithm='HS256')

    for key, user in data['users'].items():
        if user['u_id'] == u_id and user['loggedin'] == True:
            return True
        else:
            pass

    return False            

   

    
