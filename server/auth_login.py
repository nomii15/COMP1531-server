##auth_login definition
from email_check import email_check
# import the function and the global dictionary
from auth_register import *
from flask import Flask, request
from json import dumps
import jwt
import hashlib


'''
Given a registered users' email and password and generates a valid token for the user to remain authenticated

ValueError when:
Email entered is not a valid email
Email entered does not belong to a user
'''

APP = Flask(__name__)



#@APP.route('/auth/login', methods=['POST'])
def auth_login():
    
    email = request.form.get('email')
    password = request.form.get('password')

    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")
        

    # find the user
    #data = getData()
    #print(data['users'])
    i = 0
    data = getData()
    print("============")
    print(data)
    print("============")
    for user in data['users'][i]:
        print(user)
        if user['email'] == email:
            if user['password'] == hashlib.sha256(password.encode()):
                # login and break
                ret = {}
                u_id = user['name_first'].lower() + user['name_last'].lower()
                u_id = ''.join(u_id)

                # if the u_id is greater than 20 character, reduce
                if len(u_id)>20:
                    u_id = u_id[0:19]
                ret['token'] = jwt.encode({'u_id': ret['u_id']}, SECRET, algorithm='HS256').decode('utf-8')
                return dumps(ret)
            else:
                raise ValueError("Invalid Password")
        else:
            pass
        i+=1    

    raise ValueError("Incorrect Email address")
    # if get to here, email isnt associated with an account
    # return error, email not associated with a account
    
    
    
