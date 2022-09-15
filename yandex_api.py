import requests
from pprint import pprint
import json

class YaUploader:
  token = 'AQAAAAAwpuf7AADLW5z4EHRe1kzBjmjTAQ06Bg4'

  def __init__(self, folder_path):
    self.folder_path = folder_path
  def new_folder(self):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'OAuth {}'.format(self.token)}
    params = {'path': self.folder_path}
    try:
      res = requests.put(url, headers=headers, params=params)
      res.raise_for_status()
    except:
      pass
    if res.status_code == 201:
      return 'Папка создана на Я.Диск'
    if res.status_code == 409:
      return "Ошибка 409, возможно папка уже существует, либо в названии папки есть /"
    return f'Ошибка {res.status_code}'



if __name__ == '__main__':
  folder = input('Новая яндекс-папка: ')
  uploader = YaUploader(folder)
  print(uploader.new_folder())