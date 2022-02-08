from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#Initialize the database
db = SQLAlchemy(app)
ma = Marshmallow(app)

#create db model
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    cellphone = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)

#create a function to return a string when we add someone
    def __init__(self, name, address, cellphone, date):
        self.name = name
        self.address = address 
        self.cellphone = cellphone
        self.date = date
        
class FriendSchema(ma.Schema):
    class Meta:
        fields = ('name', 'address', 'cellphone', 'date')
        
friend_schema = FriendSchema()
friends_schema = FriendSchema(many=True)

@app.route('/friend', methods=["POST"])
def add_friend():
    name = request.json['name']
    address = request.json['address']
    cellphone = request.json['cellphone']
    date = request.json['date']
    
    new_friend = Friend(name, address, cellphone, date)

    db.session.add(new_friend)
    db.session.commit()

    friend = Friend.query.get(new_friend.id)

    return friend_schema.jsonify(friend)

# Endpoint to query all friends
@app.route("/friends", methods=["GET"])
def get_friends():
    all_friends = Friend.query.all()
    result = friends_schema.dump(all_friends)
    return jsonify(result)

# Endpoint for querying a single friend
@app.route("/friend/<id>", methods=["GET"])
def get_friend(id):
    friend = Friend.query.get(id)
    return friend_schema.jsonify(friend)

# Endpoint for updating a friend
@app.route("/friend/<id>", methods=["PUT"])
def friend_update(id):
    friend = Friend.query.get(id)
    name = request.json['name']
    address = request.json['address']
    cellphone = request.json['cellphone']
    date = request.json['date']

    friend.name = name
    friend.address = address
    friend.cellphone = cellphone
    friend.date = date

    db.session.commit()
    return friend_schema.jsonify(friend)

if __name__ == '__main__':
    app.run(debug=True)
        
        





