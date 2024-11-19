import requests


params = {
    "M": "",
    "lang": "ru",
    "n": "",
    "q": "",
    "T": "",
}
place = input("напишите город")
url_template = 'https://wttr.in/{}'
url = url_template.format(place)
response = requests.get(url, params=params)
response.raise_for_status()
print(response.text)
