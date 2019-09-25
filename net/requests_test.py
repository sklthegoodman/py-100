'''
requests库
    - 使用这个库来下载一些图
'''
import requests
from threading import Thread
from pprint import pprint
import os

api_url = 'https://www.mxnzp.com/api/image/girl/list/random'

class DownLaod(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/') + 1: ]
        response = requests.get(self._url)
        with open('/Users/wrynnsun/Desktop/git/py-100/net/img/' + filename, 'wb') as f:
            f.write(response.content)

def get_current_dir():
    print(__file__)
    return os.path.split(os.path.realpath(__file__))[0]

def main():
    response = requests.get(api_url)
    data = response.json()

    for obj in data['data']:
        imgUrl = obj['imageUrl']
        DownLaod(imgUrl).start()


if __name__ == "__main__":
    main()
    # print(__file__)
    # print(get_current_dir())