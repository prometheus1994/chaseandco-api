from flask import Flask, jsonify
from flask_cors import CORS
from PIL import Image
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# try:
#     evan_pic = Image.open('./images/evan-pic-01.jpg')
#     chase_pic = Image.open('./images/chase-pic-01.jpg')
# except IOError:
#     pass

members = [
    {
        'pic': '/img/chase-pic-01.3c530bb0.jpg',
        'name': 'Chase Holton',
        'title':'Singer/Songwriter', 
        'bio': 'Wichita native, Kansas raised',
        'media_handles': ['Twitter: @Chasewholton', 'Insta: @Chaseholton1', 'Facebook: @Chase Holton'],
    },
    {
        'name': 'Joseph Webster',
        'title':'Lead Guitarist', 
        'bio': 'Born in El Dorado, KS',
        'media_handles': ['Insta: @merriam.webster.94', 'Facebook: @Joseph Webster'],
    },
    {
        'pic' : '/img/evan-pic-01.2931df6e.jpg',
        'name': 'Evan Van Arsdale',
        'title':'Bassist', 
        'bio': 'Born in Wichita, KS; Raised in El Dorado, KS',
        'media_handles': ['Twitter: @evan_vanarsdale','Insta: @evan.vanarsdale','Facebook: @Evan Van Arsdale'],
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!')

@app.route('/members', methods=['GET'])
def get_members():
    response_object = {'status':'success'}
    response_object['members'] = members
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()