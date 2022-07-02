import requests


class VkUser:
    base_url = 'https://api.vk.com/method/'


    def __init__(self, user_id: int, access_token: str, version: str='5.131') -> None:
        self.params = {
            'owner_id': user_id,
            'access_token': access_token,
            'extended': 1,
            'v': version
        }
    
    # def get_album(self):
    #     url = f'{self.base_url}photos.getAlbums'
    #     params = {'need_system': 1, **self.params}
    #     res = requests.get(url, params=params)
    #     data = res.json()
    #     print('Доступные альбомы:')
    #     for item in data['response']['items']:
    #         print(f'{item["id"]}\n{item["title"]}', end='\n\n')

    #     album_ids = input('Введите через запятую id альбомов для запроса: ')
    #     return album_ids

    def write_to_json_file(self, photos):
        #пропишите логику загрузки
        ...
    
    def get_photos(self, photos_count=5):
        url = f'{self.base_url}photos.get'
        # album_ids = self.get_album()
        params = {'count': photos_count, 'album_id': 'profile', 'photo_sizes': 1, **self.params}
        res = requests.get(url, params=params)
        data = res.json()
        photos = []
        names = []
        for item in data['response']['items']:
            date = item['date']
            likes_count = item['likes']['count']
            name = f'{likes_count}.jpg'
            if name in names:
                name = f'{likes_count}_{date}.jpg'
            names.append(name)
            largest_photo = max(item['sizes'], key=lambda i: i['width'] * i['height'])
            photos.append({'name': name, 'url': largest_photo['url'], 'type': largest_photo['type']})
        self.write_to_json_file(photos)
        return photos
