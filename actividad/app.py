from flask import Flask, jsonify, request

from config import config
from models import db, User


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


enviroment = config['development']
app = create_app(enviroment)


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [user.json() for user in User.query.all()]
    return jsonify({'users': users})


@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    json = request.get_json(force=True)

    if json.get('username') is None:
        return jsonify({'message': 'Bad request'}), 400

    user = User.create(json['username'])

    return jsonify({'user': user.json()})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
