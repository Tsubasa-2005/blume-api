import json

def encode(data):
    json_data = json.dumps({'data': data})
    return json_data