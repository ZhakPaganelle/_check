import requests

for i in range(3300, 10000):
    url = 'https://events.webinar.ru/api/event/402' + str(i)
    r = requests.get(url)
    if '2020-04-18T10:10:00+0300' in r.text:
        print(r.url)
