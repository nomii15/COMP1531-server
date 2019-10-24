from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *
from email_check.py import email_check

@App.route('/user/profile/setmail', method=['PUT'])
def user_profile_setmail():
    data = getData()
    token = request.form.get('token')
    email = request.form.get('email')
    
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid email address")
    
    for user in data['users']:
        if user['email'] == email:
            raise ValueError("email address has been used")
            
    SECRET = getSecret()
        
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    
    u_id = Payload['u_id']
    
    for user in data['users']:
        if user['u_id'] == u_id:
            user['email'] = email
            
