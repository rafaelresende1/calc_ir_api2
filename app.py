from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
import pymysql

from resources.user import UserLogin


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'Segredo'
api = Api(app)

jwt = JWTManager(app)


api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    app.run()
