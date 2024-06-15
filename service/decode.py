import base64

def decode(encoded_image_data):
    encoded_image_data = encoded_image_data['image']
    image_data = base64.b64decode(encoded_image_data)
    
    with open('output_image.jpg', 'wb') as f:
        f.write(image_data)

    print('Image saved as output_image.jpg')
    return image_data