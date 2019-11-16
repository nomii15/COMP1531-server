#definition of the auth_passwordreset_reset function
from flask import Flask, request, Blueprint
from flask_mail import Mail, Message
from json import dumps
from email_check import email_check
import random
import string
import hashlib
from data import *
'''
Given a reset code for a user, set that user's new password to the password provided

ValueError when:
reset_code is not a valid reset code
Password entered is not a valid password
'''
def auth_passwordreset_reset(reset_code,new_password):

    #check new password to see if its valie    
    if len(new_password) < 5 or len(new_password) == 0:
        raise ValueError(description = "Invalid Password Length")

    # get the reset code for the user requesting reset
    global reset
    reset = getReset()

    global data
    data = getData()

    for j in reset['codes']:
        #print(j)
        if j['code'] == reset_code:
            # find the user for that reset code
            for i, item in data['users'].items():
                if item['u_id'] == j['u_id']:
                    item['password'] = hashlib.sha256(new_password.encode())
                    reset['codes'].remove(j)
                    return {}

    raise ValueError(description = "Incorrect Reset Code")
            


reset = Blueprint('reset', __name__)
@reset.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():

    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    return dumps( auth_passwordreset_reset(reset_code,new_password) )