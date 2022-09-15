import unittest
import requests
from unittest.mock import patch
import yandex_api

class TestYandex(unittest.TestCase):
    token = 'AQAAAAAwpuf7AADLW5z4EHRe1kzBjmjTAQ06Bg4'

    def test_YaUploader_new_folder_1(self):
        #Проверка кода ответа
        uploader = yandex_api.YaUploader('TEST')
        result = uploader.new_folder()
        self.assertEqual("Папка создана на Я.Диск", result)

    def test_YaUploader_new_folder_1_1(self):
        #Проверка кода ответа
        uploader = yandex_api.YaUploader('/TEST')
        result = uploader.new_folder()
        self.assertEqual("Ошибка 409, возможно папка уже существует, либо в названии папки есть /", result)

    def test_YaUploader_new_folder_2(self):
        #Есть ли папка
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': "disk:/"}
        result = requests.get(url, headers=headers, params=params).json()
        dirs = []
        for item in result['_embedded']['items']:
            if item['type'] == 'dir':
                dirs.append(item['name'])
        self.assertIn("TEST", dirs, 'Папка не была создана')

        #Удаление тестовой папки
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': "disk:/TEST"}
        requests.delete(url, headers=headers, params=params)

if __name__ == '__main__':
    unittest.main()