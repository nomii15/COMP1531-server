from data import *
from token_check import token_check
from users_all import users_all
from auth_register import auth_register
import pytest
import jwt

#invalid token
def test_users_all1():
    #generate a dodgy token
    global SECRET
    SECRET = getSecret()
    token = jwt.encode({'u_id':-1}, SECRET, algorithm='HS256').decode('utf-8')
    #fails as token is not valid
    with pytest.raises(ValueError, match = "Invalid Token"):
        users_all(token)

#successful
def test_users_all2():
    #generate a test login
    register = auth_register("z5110036@unsw.edu.au", "1234567", "John", "Smith")
    re2 = auth_register("z5110046@unsw.edu.au", "hellod", "John", "Smith")
    re3 = auth_register("z5110056@unsw.edu.au", "1234567", "John", "Smith")
    
    #get the token
    token = register['token']
    u_id = register['u_id']

    user1 = False
    user2 = False
    user3 = False

    users = users_all(token)
    # checking to see if all users are in the list
    for i in users['users']:
        if i['u_id'] == u_id:
            user1 = True
        elif i['u_id'] == re2['u_id']:
            user2 = True
        elif i['u_id'] == re3['u_id']:
            user3 = True
    assert user1 and user2 and user3       

