#definition auth_register function
from email_check import email_check
from flask import Flask, request, Blueprint, jsonify
import string
import jwt
import hashlib
from json import dumps
from werkzeug.exceptions import HTTPException

# importing the data file
from data import *


'''
Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session

ValueError when:
Email entered is not a valid email.
Email address is already being used by another user
Password entered is not a valid password
name_first is more than 50 characters
name_last is more than 50 characters
'''


def auth_register(email, password, name_first, name_last):
    
    #check if valid email
    if email_check(email) == "Invalid Email":
        raise ValueError(description = "Invalid Email Address")

    #password length check
    if len(password) < 5:
        raise ValueError(description = "Invalid Password Length")
        
    #first name length check    
    if len(name_first) > 50 or len(name_first) == 0:
        raise ValueError(description = "Invalid First Name Length")
    
    #last name length check   
    if len(name_last) > 50 or len(name_last) == 0:
        raise ValueError(description = "Invalid Last Name Length")


    # add user dictionary to add to the global dictionary

    # create new user to the data dictionary, need to check syntax
    global data
    data = getData()

    # check to see if the email is already registered
    for em,pas in data['users'].items():
        if pas['email'] == email:
            raise ValueError(description = "Email already exists")

    # if it gets here, its a valid user
    global user
    user = getUsers()


    handle = name_first.lower() + name_last.lower()
    handle = ''.join(handle)

    # if the u_id is greater than 20 character, reduce
    if len(handle)>17:
        handle = handle[0:17]

    # also add number to reduce handle conflicts
    handle = handle + str(user)
    handle = ''.join(handle)

    if len(handle) > 20:
        handle = handle[0:19]

    u_id = int(user)

    data['users'][user] = {'email': email, 'password': hashlib.sha256(password.encode()), 'name_first': name_first,
     'name_last': name_last, 'u_id': u_id, 'loggedin': True, 'handle': handle, 'profile_img_url': None}
    incUser()

    #think about implementing a variable for u_id within data
    #currently, two names may clash

    # return a dictionary of u_id and token
    #ret = {}

   

    global SECRET
    SECRET = getSecret()

    #ret['u_id'] = u_id
    token = jwt.encode({'u_id':u_id}, SECRET, algorithm='HS256').decode('utf-8')
    #ret  = dict()
    #ret['u_id'] = u_id
    #ret['token'] = token
    #ret = {'token':token, 'u_id': u_id}   
    
    #print(ret)
    return {
        'u_id': u_id,
        'token': token
    }


register = Blueprint('register', __name__)

@register.route('/auth/register', methods=['POST'])
def auth_reg_route():
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    return dumps( auth_register(email, password, name_first, name_last) )