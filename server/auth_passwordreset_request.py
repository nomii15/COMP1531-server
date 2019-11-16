#definition of the auth_passwordreset_request function

#base for this function comes from the sample code provided (myemail.py)

from flask import Flask, request, Blueprint, current_app as APP
from flask_mail import Mail, Message
from json import dumps
from email_check import email_check
import random
import string
import hashlib
from data import data, getData, reset, getReset



'''
Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.


N/A
'''
def auth_passwordreset_request(Email):   
    
    #invalid email entered
    if email_check(Email) == "Invalid Email":
        raise ValueError(description = "Invalid Email Address")
    
    global data
    data = getData()
    check = 0
    for j, items in data['users'].items():
        if items['email'] == Email:
            check = 1

    if check!=1:
        raise ValueError(description = "Not a Registed Email Address")
 
    mail = Mail(APP)
    APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'DJMN1531@gmail.com',
    MAIL_PASSWORD = "password1531"
                )

    # generate a code
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    mesg = Message("Reset Code: ")
    # look through the data to see if the email is there
    for i, items in data['users'].items():
        #print(item['email'])
        if items['email'] == Email:
            #print(item['email'])
            # send the code to reset the password
            mesg.sender = "DJMN1531@gmail.com"
            mesg.recipients = [items['email']]
            mesg.body = code
            # store the code to reset password
            try:
                #print("mail sent")
                mail.send(mesg)
            except Exception as e:
                # add a raise for when the message reset wasnt sent though
                raise AccessError(description = "not sent, try again")
            global reset
            reset = getReset()
            reset['codes'].append({'u_id': items['u_id'], 'code': code})
            return {}







requestR = Blueprint('requestR', __name__)

@requestR.route('/auth/passwordreset/request', methods=['POST'])
def passwordreset_request():

    Email = request.form.get('email')
    return dumps( auth_passwordreset_request(Email) )