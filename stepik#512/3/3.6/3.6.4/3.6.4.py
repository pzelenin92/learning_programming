import requests
import json

client_id = 'ef2277979a2857c02f86'
client_secret = 'a98dca5ee0a0a423a946e4038e967f21'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                    data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)# разбираем ответ сервера
token = j["token"]# достаем токен
headers = {"X-Xapp-Token" : token}# создаем заголовок, содержащий наш токен
template="https://api.artsy.net/api/artists/{}" #шаблон-ссылка
d={}
with open("dataset_24476_4.txt", "r") as inputdataset:
    for line in inputdataset:
        url=template.format(line.rstrip()) #подставляем в шаблон-ссылку значение из текстового файла в {}
        r = requests.get(url, headers=headers)# инициируем запрос с заголовком
        j = json.loads(r.text)# разбираем ответ сервера
        birthday, name=j["birthday"], [j["sortable_name"]]
        if birthday in d:
            d[birthday]=d[birthday]+name
        else:
            d[birthday]=name

for k in sorted(d):
    for v in sorted(d[k]):
        print(v)

