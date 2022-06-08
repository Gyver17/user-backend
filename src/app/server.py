from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from jsonschema import ValidationError
from flask_cors import CORS
from app.routes.user import users
from const.config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# Settings
CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)


app.register_blueprint(users)
# app.register_blueprint(auth)

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return jsonify({'error': original_error.message}), 400

    #return error
    return error

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': error}), 500