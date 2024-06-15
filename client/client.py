import os
import requests
import base64

base_url = os.environ['BASE_URL']
headers = {'Content-Type': 'application/json'}

def ping_server():
    """サーバーの生存確認を行う"""
    response = requests.get(f'{base_url}/ping', headers=headers)
    if response.ok:
        print('ping: ', response.json())
    else:
        print(f'Error pinging server. Status code: {response.status_code}, Response: {response.text}')

def encode():
    data = {
        'letter': str(input('letter: ')),
    }
    response = requests.post(f'{base_url}/encode', headers=headers, json=data)
    if response.ok:
        print('res_encode: ', response.json())
    else:
        print(f'Encoding failed. Status code: {response.status_code}, Response: {response.text}')

def decode():
    image_path = "image/1.png"
    with open(image_path, 'rb') as f:
        image_data = f.read()
    encoded_image_data = base64.b64encode(image_data).decode('utf-8')
    data = {'image': encoded_image_data}

    data = {
        'image': encoded_image_data,
    }
    response = requests.post(f'{base_url}/decode', headers=headers, json=data)
    if response.ok:
        print('res_decode: ', response.json())
    else:
        print(f'Decoding failed. Status code: {response.status_code}, Response: {response.text}')

def main():
    ping_server()
    encode()
    decode()


if __name__ == '__main__':
    main()