#definition of the auth_passwordreset_reset function

'''
Given a reset code for a user, set that user's new password to the password provided

ValueError when:
reset_code is not a valid reset code
Password entered is not a valid password
'''

def auth_passwordreset_reset(reset_code, new_password):
    
    #dummy code to check for email reset
    if reset_code != "AUW624":
        raise ValueError("Incorrect Reset Code")
    
    #check new password to see if its valie    
    if len(new_password) < 5 or len(new_password) == 0:
        raise ValueError("Invalid Password Length")
    
    #dummy check for successful     
    return "Password Reset"          
