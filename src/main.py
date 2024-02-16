import sys
import requests

REQUEST_URL = 'https://zipcloud.ibsnet.co.jp/api/search'

def get_zipcloud(zipcode):
    """郵便番号から住所情報を取得

    Args:
        zipcode (str): 郵便番号

    Returns:
        dict: 郵便番号に関連する住所情報を含むJSONレスポンス
    """
    res = requests.get(REQUEST_URL, params={'zipcode': zipcode})
    return res.json()

def get_address(data):
    """住所情報から住所を取得

    Args:
        data (dict): 住所情報を含むJSONデータ

    Returns:
        str: 住所
    """
    if data['results'] != None:
        results = data['results'][0]
        return results['address1'] + results['address2'] + results['address3']
    return 'Not found address.'

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        print(get_address(get_zipcloud(args[1])))