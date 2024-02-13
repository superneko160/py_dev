import sys
import requests

REQUEST_URL = 'https://zipcloud.ibsnet.co.jp/api/search'

def get_zipcloud(zipcode):
    res = requests.get(REQUEST_URL, params={'zipcode': zipcode})
    return res.json()

def get_address(data):
    if data['results'] != None:
        results = data['results'][0]
        return results['address1'] + results['address2'] + results['address3']
    return 'Not found address.'

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        print(get_address(get_zipcloud(args[1])))