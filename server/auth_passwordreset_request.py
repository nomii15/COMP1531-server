#definition of the auth_passwordreset_request function

#base for this function comes from the sample code provided (myemail.py)

from flask import Flask, request, Blueprint, current_app as APP
from flask_mail import Mail, Message
from json import dumps
from email_check import email_check
import random
import string
import hashlib
from data import *




'''
Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.


N/A
'''

requestR = Blueprint('requestR', __name__)

@requestR.route('/auth/passwordreset/request', methods=['POST'])
def auth_passwordreset_request():

    email = request.form.get('email')
    
    
    mail = Mail(APP) 
    
    APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'DJMN1531@gmail.com',
    MAIL_PASSWORD = "password1531"  
                    )
    
    
                

    
    #invalid email entered
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")

    global data
    data = getData()

    # generate a code
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    # look through the data to see if the email is there
    for id, item in data['users'].items():
        #print(item['email'])
        if item['email'] == email:
            #print(item['email'])
            # send the code to reset the password
            try:
                msg = Message("Reset code: ",
                    sender="DJMN1531@gmail.com",
                    recipients=[ item['email'] ])

                  
                msg.body = code
                mail.send(msg)
                # store the code to reset password
                global reset
                reset = getReset()
                reset['codes'] = {'u_id': item['u_id'], 'code': code}
                print("mail sent")
                return dumps({})
            except Exception as e:
                print("not sent")
                print(str(e))
                return (str(e))        
                       

            # break

    # if it gets to here, email not registered                 
    raise ValueError("Not a Registed Email Address")



