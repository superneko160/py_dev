from src import main

def test_get_zipcloud():
    result = {
        'message': None,
        'results': [
            {
                'address1': '東京都',
                'address2': '千代田区',
                'address3': '永田町',
                'kana1': 'ﾄｳｷｮｳﾄ',
                'kana2': 'ﾁﾖﾀﾞｸ',
                'kana3': 'ﾅｶﾞﾀﾁｮｳ',
                'prefcode': '13',
                'zipcode': '1000014'
            }
        ],
        'status': 200
    }
    assert result == main.get_zipcloud('100-0014')

def test_fail_get_zipcloud():
    result = {
        "message": "パラメータ「郵便番号」の桁数が不正です。",
        "results": None,  # ブラウザ上などで確認するとnullだがpython通した段階でNoneに変わる
        "status": 400
    }
    assert result == main.get_zipcloud('1')

def test_get_address():
    result = '東京都千代田区永田町'
    data = {
        'message': None,
        'results': [
            {
                'address1': '東京都',
                'address2': '千代田区',
                'address3': '永田町',
                'kana1': 'ﾄｳｷｮｳﾄ',
                'kana2': 'ﾁﾖﾀﾞｸ',
                'kana3': 'ﾅｶﾞﾀﾁｮｳ',
                'prefcode': '13',
                'zipcode': '1000014'
            }
        ],
        'status': 200
    }
    assert result == main.get_address(data)

def test_fail_get_address():
    result = 'Not found address.'
    data = {
        "message": "パラメータ「郵便番号」の桁数が不正です。",
        "results": None,  # ブラウザ上などで確認するとnullだがpython通した段階でNoneに変わる
        "status": 400
    }
    assert result == main.get_address(data)