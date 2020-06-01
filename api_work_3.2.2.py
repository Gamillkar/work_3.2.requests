import requests
import os
def save_translaite_in_iandex_could(name_file):
    token = "OAuth AgAAAAA-ZeNAAADLWxuQy00OGkimm35Jyk1yEp0"
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    file = {'file': open(f'transfer/{name_file}')}

    headers = {'Accept': 'application/json', "Authorization": token}
    params = {'path': f'/{name_file}'}

    response = requests.get(URL, headers=headers, params=params)

    upload_url = response.json()['href']

    upload_file = requests.put(upload_url, headers=headers, files=file)

    print(upload_file)

#интерация по файлам из папки transfer. Запуск функции.
name_file = os.listdir('transfer')
for file in name_file:
    save_translaite_in_iandex_could(file)




