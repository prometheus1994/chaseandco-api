from flask import Flask, jsonify
from flask_cors import CORS
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Member:
    def __init__(self, name, title, bio, media_handles):
        self.name = name
        self.title = title
        self.bio = bio
        self.media_handles = media_handles

members = [
    {
        'name': 'Chase Holton',
        'title':'Front man for Chase&Co.', 
        'bio': 'Wichita native, Kansas raised',
        'media_handles': ['@Chasewholton', '@Chaseholton1', '@Chase Holton'],
    },
    {
        'name': 'Joseph Webster',
        'title':'Lead guitarist for Chase&Co.', 
        'bio': 'Born in El Dorado, KS',
        'media_handles': ['@wut'],
    },
    {
        'name': 'Evan Van Arsdale',
        'title':'Bassist for Chase&Co.', 
        'bio': 'Born in Wichita, KS; Raised in El Dorado, KS',
        'media_handles': ['@evan.vanarsdale','@evan_vanarsdale','@Evan Van Arsdale'],
    }

    # Member('Chase Holton', 
    #        'Front man for Chase&Co.', 
    #        'Wichita native, Kansas raised',
    #        ['@Chasewholton', '@Chaseholton1', '@Chase Holton']),
    # Member('Evan Van Arsdale',
    #        'Bassist for Chase&Co.',
    #        'Born in Wichita, KS; Raised in El Dorado, KS',
    #        ['@evan.vanarsdale','@evan_vanarsdale','@Evan Van Arsdale']),
    # Member('Joseph Webster',
    #        'Lead guitarist for Chase&Co.',
    #        'Born and Raised in El Dorado, KS',
    #        ['@something'])
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