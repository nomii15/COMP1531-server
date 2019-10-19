#definition of the auth_passwordreset_request function

#base for this function comes from the sample code provided (myemail.py)

from flask import Flask
from flask_mail import Mail, Message

from email_check import email_check
from data import *




'''
Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.


N/A
'''


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

    # look through the data to see if the email is there
    for id, item in data['users'].items():
        if item['email'] == email:
            # send the code to reset the password
            try:
                msg = Message("Send Mail Test!",
                    sender="DJMN1531@gmail.com",
                    recipients=[item['email']])
                # get a better reset code , maybe a random number generator   
                msg.body = "123456"
                mail.send(msg)
                return dumps({})
            except Exception as e:
                return (str(e))        

            

            # break

    # if it gets to here, email not registered                 
    raise ValueError("Not a Registed Email Address")
     
    
