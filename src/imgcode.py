import base64

def encode_img(img_path):
    with open(img_path, 'br') as f:
        data = base64.b64encode(f.read())
    return data

def decode_data(data):
    return base64.b64decode(data)

if __name__ == '__main__':
    print(encode_img('images/dummy_image.jpg'))