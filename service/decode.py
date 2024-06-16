import base64
from . import line_drawing as decode_draw
from . import triming as decode_trim
from . import output as decode_output
from . import message
import numpy as np
from flask import jsonify
import json

def post_decode(encoded_image_data):
    encoded_image_data = encoded_image_data['image']
    image_data = base64.b64decode(encoded_image_data)
    
    with open('output_image.jpg', 'wb') as f:
        f.write(image_data)

    print('Image saved as output_image.jpg')

    
    new_distances = decode_output.get_distances()

    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []

    print(new_distances)

    for distance in new_distances:
        x1.append(distance[0])
        x2.append(distance[0])
        x3.append(distance[0])
        y1.append(distance[1][0] / 10 + 0.1)
        y2.append(distance[1][1] * 0.075 + 0.02)
        y3.append(distance[1][2] * 0.05 - 0.05)
  
    a1 = message.decode(x1, y1)
    a2 = message.decode(x2, y2)
    a3 = message.decode(x3, y3)

    print(a1)
    print(a2)
    print(a3)

    return jsonify({'decode1': a1
                    , 'decode2': a2
                    , 'decode3': a3})


