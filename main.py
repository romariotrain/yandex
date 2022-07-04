import requests

from pprint import pprint

import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type' : 'application/json',
            'Authorization' : 'OAuth {}'.format(self.token)
        }
    def upload(self, file_path):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(URL, headers=headers, params=params)
        pprint(response.json())
        return response.json()


    def upload_file_to_disk(self, file_path):
        response_href = self.upload(file_path)
        href = response_href.get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        file_path = os.path.normpath(file_path)
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':

    token = ''


    ya = YaUploader(token)
    ya.upload_file_to_disk('388908-sepik.jpg')