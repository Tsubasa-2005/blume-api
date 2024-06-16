import json

def post_encode(data):
    json_data = json.dumps({'data': data})
    return json_data