#definition of the auth_passwordreset_request function

#base for this function comes from the sample code provided (myemail.py)

from flask import Flask, request
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

APP = Flask(__name__)

#request = Blueprint('request', __name__)

#@register.route('/auth/passwordreset/request', methods=['POST'])
@APP.route('/auth/passwordreset/request', methods=['POST'])
def auth_passwordreset_request():

    email = request.form.get('email')

    APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'DJMN1531@gmail.com',
    MAIL_PASSWORD = "password1531"  
                    )

    mail = Mail(APP)                

    
    #invalid email entered
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")

    global data
    data = getData()
    

    data['users'][0] = {'email': 'daniel-setkiewicz@hotmail.com.au', 'password': 'password', 'name_first': 'daniel',
     'name_last': 'setkiewicz', 'u_id': 'danset', 'loggedin': True}

    # generate a code
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    # look through the data to see if the email is there
    for id, item in data['users'].items():
        print(item['email'])
        if item['email'] == email:
            # send the code to reset the password
            try:
                msg = Message("Reset code: ",
                    sender="DJMN1531@gmail.com",
                    recipients=[item['email']])
                # get a better reset code , maybe a random number generator   
                msg.body = code
                mail.send(msg)
                # store the code to reset password
                global reset
                reset = getReset()
                reset['codes'] = {'u_id': item['u_id'], 'code': code}
                return dumps({})
            except Exception as e:
                return (str(e))        
                       

            # break

    # if it gets to here, email not registered                 
    raise ValueError("Not a Registed Email Address")


#@register.route('/auth/passwordreset/request', methods=['POST'])
@APP.route('/auth/passwordreset/reset', methods=['POST'])
def auth_passwordreset_reset():

    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    
    #check new password to see if its valie    
    if len(new_password) < 5 or len(new_password) == 0:
        raise ValueError("Invalid Password Length")

    # get the reset code for the user requesting reset
    global reset
    reset = getReset()

    global data
    data = getData()

    for i, j in reset.items():
        #print(j)
        if j['code'] == reset_code:
            # find the user for that reset code
            for id, item in data['users'].items():
                if item['u_id'] == j['u_id']:
                    item['password'] = hashlib.sha256(new_password.encode())
                    del(j)
                    return dumps({})

    raise ValueError("Incorrect Reset Code")
     
    
if __name__ == '__main__':
    APP.run(port=20000, debug=True)

