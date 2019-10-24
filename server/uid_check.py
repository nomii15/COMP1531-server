# check to see if a u_id is valid

# importing the data file
from data import *

def uid_check(u_id):

    global data
    data = getData()

    for key, item in data['users'].items():
        if item['u_id'] == u_id:
            if item['loggin'] == True:
                return True

    return False            
    