from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
import pymysql

from db import db
from resources.user import UserLogin

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rafa:477075@18.217.230.166/calc_ir'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'Segredo'
api = Api(app)

jwt = JWTManager(app)


api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)