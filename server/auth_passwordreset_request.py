#definition of the auth_passwordreset_request function

from email_check import *

'''
Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.


N/A
'''

def auth_passwordreset_request(email):
    
    #invalid email entered
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")  
          
    #check if the email address is registered    
    raise ValueError("Not a Registed Email Address")
    
    #if it gets here it should send a code to the email   
    
