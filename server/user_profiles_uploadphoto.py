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

    # add checks to see if that values are correct inputs
    urllib.request.urlretrieve(img_url, f"./server/{u_id}.png")

    #crop the url image
    imageobject = Image.open(f"./server/{u_id}.png")
    cropped = imageobject.crop((x_start,x_end,y_start,y_end))
    cropped.save(f"./server/{u_id}.png")
    

    #save img url in users details
    for i, items in data['users'].items():
        if items['u_id'] == u_id:
            items['profile_img_url'] = f"./server/{u_id}.png"
            break
    
    return {}





uploadphoto = Blueprint('uploadphoto', __name__,static_url_path='/server/')
@uploadphoto.route('/user/profiles/uploadphoto', methods=['POST'])
def upload():
    token = request.form.get('token')
    img_url = str(request.form.get('img_url'))
    x_start = int(request.form.get('x_start'))
    x_end = int(request.form.get('x_end'))
    y_start = int(request.form.get('y_start'))
    y_end = int(request.form.get('y_end'))
    users_profiles_uploadphoto(token, img_url, x_start, x_end, y_start, y_end)
    send_from_directory('', "server/1.png")

    return dumps( {} )