from data import *
import jwt
from flask import Flask, request, Blueprint, send_from_directory
from json import dumps
import urllib.request
import sys
from PIL import Image

def users_profiles_uploadphoto(token, img_url, x_start, x_end, y_start, y_end):
    
    # retrieve u_id from token
    global SECRET 
    SECRET = getSecret()
    token_payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = token_payload['u_id']

    port = sys.argv[1]
    url = f"http://127.0.0.1:{port}/static/"
    name = f"{u_id}.png"
    # add checks to see if that values are correct inputs
    urllib.request.urlretrieve(img_url, "./static/"+name)

    #crop the url image
    imageobject = Image.open("./static/"+name)
    cropped = imageobject.crop((x_start,x_end,y_start,y_end))
    cropped.save("./static/"+name)

    #print("get here")

    #save img url in users details
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            items['profile_img_url'] = url + name
            #print(items['profile_img_url'])
            break

    #send to server
         
    
    return





uploadphoto = Blueprint('uploadphoto', __name__)
@uploadphoto.route('/user/profiles/uploadphoto', methods=['POST'])
def upload():

    token = request.form.get('token')
    img_url = str(request.form.get('img_url'))
    x_start = int(request.form.get('x_start'))
    x_end = int(request.form.get('x_end'))
    y_start = int(request.form.get('y_start'))
    y_end = int(request.form.get('y_end'))
    users_profiles_uploadphoto(token, img_url, x_start, x_end, y_start, y_end)
    return dumps( {} )
