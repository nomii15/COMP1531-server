# storing of lists for variables accross multiple functions

global SECRET
SECRET = 'COMP1531'

global user
user = 0

global data
data = {
    'users': {} 
}

def getData():
    global data
    return data

def getSecret():
    global SECRET
    return SECRET    

def getUsers():
    global user
    return user

def incUser():
    global user
    user+=1        
