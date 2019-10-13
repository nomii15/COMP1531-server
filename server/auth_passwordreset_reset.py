#definition of the auth_passwordreset_reset function
import auth_register 
import auth_passwordreset_request
import auth_register
'''
Given a reset code for a user, set that user's new password to the password provided

ValueError when:
reset_code is not a valid reset code
Password entered is not a valid password
'''

# need to store the code to compare at a later date

def auth_passwordreset_reset(reset_code, new_password):
    
    #dummy code to check for email reset
    if reset_code != global auth_passwordreset_request.code:
        raise ValueError("Incorrect Reset Code")
    
    #check new password to see if its valie    
    if len(new_password) < 5 or len(new_password) == 0:
        raise ValueError("Invalid Password Length")

    #update the changed variables
    # need to check if the code variable should include the email address
    for user in global auth_register.data['email']:
        if user['email'] == global auth_passwordreset_request.code['email']:
           user['password'] = new_password
           break
        else:
            pass   

    
    
    #if it gets here the password should be successfully changed         
