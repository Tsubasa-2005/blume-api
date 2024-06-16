from flask import Blueprint
from flask import request
from service import encode, decode
from json import load
import logger
import json

# Generate Router Instance
router = Blueprint('router', __name__)

@router.route("/ping", methods=['GET'])
def ping():
    json_data = json.dumps({'pong': "pong"})
    return json_data

@router.route("/encode", methods=['POST'])
def post_encode():
    data = request.get_json()
    return encode.post_encode(data)

@router.route("/decode", methods=['POST'])
def post_decode():
    data = request.get_json()
    return decode.post_decode(data)
