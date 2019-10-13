#definition of the auth_passwordreset_request function

from email_check import email_check
import auth_register 

'''
Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.


N/A
'''
global code

def auth_passwordreset_request(email):
    
    #invalid email entered
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid Email Address")

    # look through the data to see if the email is there
    for Email in auth_register.data.items():
        if Email['email'] == email:
            # send the code to reset the password
            # need to store the request to compare later

            # break

    # if it gets to here, email not registered                 
    raise ValueError("Not a Registed Email Address")
     
    
