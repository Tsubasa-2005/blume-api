import base64
from . import line_drawing as decode_draw
from . import triming as decode_trim
from . import output as decode_output
import message
import numpy as np
from flask import jsonify
import json

def post_decode(encoded_image_data):
    encoded_image_data = encoded_image_data['image']
    image_data = base64.b64decode(encoded_image_data)
    
    with open('output_image.jpg', 'wb') as f:
        f.write(image_data)

    print('Image saved as output_image.jpg')

    decode_draw.line_drawing_image("output_image.jpg")
    decode_trim.crop_to_non_bg("line_drawing_output.jpg", "cropped_image.jpg")
    distances = decode_output.find_smallest_circle_center("cropped_image.jpg")
    new_distances = decode_output.output(distances)

    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []

    for distance in new_distances:
        x1.append(distance[0])
        x2.append(distance[0])
        x3.append(distance[0])
        y1.append(distance[1][0] / 10 + 0.1)
        y2.append(distance[1][1] * 0.075 + 0.02)
        y3.append(distance[1][2] * 0.05 - 0.05)

    degree = 300
    coefficients = np.polyfit(x1, y1, degree)
   

    coefficients = np.polyfit(x2, y2, degree)


    coefficients = np.polyfit(x3, y3, degree)
  

    a1 = message.decode(x1, y1)
    a2 = message.decode(x2, y2)
    a3 = message.decode(x3, y3)

    print(a1)
    print(a2)
    print(a3)

    #return jsonify({'decode1': decode_image.decode(x1, y1) 
    #                , 'decode2': decode_image.decode(x2, y2)
    #                , 'decode3': decode_image.decode(x3, y3)})
    return json.dumps({'data': "a"})


