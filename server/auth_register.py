#definition auth_register function
from email_check import email_check
from flask import Flask, request, Blueprint
from json import dumps
import jwt
import hashlib

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

register = Blueprint('APP_register', __name__)

@register.route('/auth/register', methods=['POST'])
def auth_register():

    
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    
    #check if valid email
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")

    #password length check
    if len(password) < 5:
        raise ValueError("Invalid Password Length")
        
    #first name length check    
    if len(name_first) > 50 or len(name_first) == 0:
        raise ValueError("Invalid First Name Length")
    
    #last name length check   
    if len(name_last) > 50 or len(name_last) == 0:
        raise ValueError("Invalid Last Name Length")


    # add user dictionary to add to the global dictionary

    # create new user to the data dictionary, need to check syntax
    global data
    data = getData()

    # check to see if the email is already registered
    for em,pas in data['users'].items():
        if pas['email'] == email:
            raise ValueError("Email already exists")

    # if it gets here, its a valid user
    global user
    user = getUsers()


    #u_id = name_first.lower() + name_last.lower()
    #u_id = ''.join(u_id)
    u_id = user

     # if the u_id is greater than 20 character, reduce
   # if len(u_id)>20:
   #     u_id = u_id[0:19]

    data['users'][user] = {'email': email, 'password': hashlib.sha256(password.encode()), 'name_first': name_first,
     'name_last': name_last, 'u_id': u_id, 'loggedin': True}
    incUser()

    #think about implementing a variable for u_id within data
    #currently, two names may clash

    # return a dictionary of u_id and token
    #ret = {}

   

    global SECRET
    SECRET = getSecret()

    #ret['u_id'] = u_id
    token = jwt.encode({'u_id':u_id}, SECRET, algorithm='HS256').decode('utf-8')
    ret  = dict()
    ret['u_id'] = u_id
    ret['token'] = token
  
    #print(ret)
    return dumps(ret)