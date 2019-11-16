import jwt
from data import SECRET, getSecret

#function to convert token into u_id
def token_to_uid(token):
    global SECRET
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id'] 
    return u_id
