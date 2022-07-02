from urllib import response
import requests
from tqdm import tqdm

class Yandex:
    base_url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def __init__(self, access_token) -> None:
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {access_token}'
        }

    def _create_folder(self):
        folder_name = input('Введите название папки для загрузки: ')
        params = {'path': folder_name}
        response = requests.put(self.base_url, params=params, headers=self.headers)
        if response.status_code == '200':
            print('Папка успешно создана')
            return folder_name
        elif response.status_code == 409:
            print('Папка уже существует. Введите новое имя')
            return self._create_folder()

    def upload_photos(self, photos):
        upload_url = f'{self.base_url}upload/' 
        folder_name = self._create_folder()
        #добавьте логику прогресс-бара
        for photo in photos:
            path = f'/{folder_name}/{photo["name"]}'
            url = photo['url']
            params = {'path': path, 'url': url}
            response = requests.post(upload_url, params=params, headers=self.headers)
            response.raise_for_status()
        print('Загрузка завершена')