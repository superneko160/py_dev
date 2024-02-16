import base64

def encode_img(img_path):
    """画像ファイルをBase64形式でエンコード

    Args:
        img_path (str): 画像ファイルのパス

    Returns:
        bytes: Base64形式でエンコードされた画像データ
    """
    with open(img_path, 'br') as f:
        data = base64.b64encode(f.read())
    return data

def decode_data(data):
    """Base64形式のデータをデコード

    Args:
        data (bytes): Base64形式のデータ

    Returns:
        bytes: デコードされたデータ
    """
    return base64.b64decode(data)

if __name__ == '__main__':
    print(encode_img('images/dummy_image.jpg'))