import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file_path, to_file_path, from_lang, to_lang='ru'):

    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(from_file_path, 'r', encoding='utf-8') as f:
        file = f.read()

    params = {
        'key': API_KEY,
        'text': file,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    json_final = ''.join(json_['text'])

    final_text = os.path.join('transfer', to_file_path)
    with open(final_text, 'w') as wr_tr:
        wr_tr.write(json_final)

if __name__ == '__main__':
    translate_it('ES.txt', 'ES-RU.txt', 'es')


