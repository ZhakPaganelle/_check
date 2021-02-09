import requests
from datetime import datetime

t = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'tmr_lvid=8c5288b658e76541c783f37789caa504; tmr_lvidTS=1585767436890; _ym_uid=1585767437906235759; _ym_d=1585767437; _ga=GA1.2.390737997.1585767439; MoodleSession=fe01ueq6vudpdohpcidg64tve1; MOODLEID1_=%25E9c%2582%255C%25A4%2Bi%2505%259F%2502%25F5L%250E%25C2; _gid=GA1.2.593220069.1586007564; tmr_reqNum=45; _ym_visorc_61559215=w; _ym_isad=2',
'Host': 'study.rea.ru',
'Referer': 'https://study.rea.ru/login/index.php',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.197 Yowser/2.5 Safari/537.36'}

url ='https://study.rea.ru/my/'

ar = []

for i in range (10):
    f = datetime.now()
    r = requests.get(url = url, headers = t)
    print(r)
    print(datetime.now() - f)
    ar.append(datetime.now() - f)
    if i == 9:
        print(r.text)


def get_seconds(date_str):
    date1 = datetime.strptime('0:00:00.000000', '%H:%M:%S.%f')
    date2 = datetime.strptime(str(date_str), '%H:%M:%S.%f')
    delta = date2 - date1
    return delta.total_seconds()

for i in range(len(ar)):
    ar[i] = get_seconds(ar[i])

print(sum(ar)/10)
