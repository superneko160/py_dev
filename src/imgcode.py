import base64

def encode_img(img_path):
    """画像ファイルをBase64形式でエンコード
    Args:
        img_path (str): 画像ファイルのパス
    Returns:
        bytes: Base64形式でエンコードされた画像データ
    """
    try:
        with open(img_path, 'br') as f:
            data = base64.b64encode(f.read())
        return data
    except Exception as e:
        print(f"Failed to encode image: {e}")
        return None

def decode_img(data):
    """Base64形式のデータをデコード
    Args:
        data (bytes): Base64形式のデータ
    Returns:
        bytes: デコードされたデータ
    """
    if data != None:
        return base64.b64decode(data)
    return None

if __name__ == '__main__':
    print(decode_img(encode_img('images/dummy_image.jpg')))