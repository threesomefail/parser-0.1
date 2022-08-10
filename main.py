import requests
from bs4 import BeautifulSoup

# Записываем в виде переменной ссылку на сам сайт
URL = 'http://allbazar.uz/cat-ovoshchi_i154/'
# Записываем в виде переменной данные нашего браузера, устройства и подтверждение входа, чтобы нас сам сайт не посчитал ботом
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0','accept':'*/*'}

# Получаем какой-то контент с помощью гет запроса и возвращаем его значение, в аргументах обязательно указываем данные нашего браузера
def get_con_to_site(url, params=None):
    gettingreqs = requests.get(url, headers=HEADERS, params=params)
    return gettingreqs


# Задействуем BeautifulSoup для парсинга
def recieve_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='top-product--price-block')

# Создаем словарь vegetables, в который будут записываться данные(название продукта и цена в суммах), обозначая класс в котором находятся данные
    vegetables = []
    for item in items:
        vegetables.append({
            'title':item.find('span', class_='top-product--price font--14-grey').get_text(strip=True),
            'price':item.find('a', class_='top-product--price font--14-black').get_text(strip=True)
        })
    print(vegetables)

# В виде переменной sitecon передаем запрос к определенному url'у, который уже был объявлен нами
def parsingapp():
    sitecon = get_con_to_site(URL)
# Если при получении запроса, код состояния не 200, то выводим в консоль ошибку
    if sitecon.status_code == 200:
        recieve_content(sitecon.text)
    else:
        print("ERROR")


# Вызываем саму программу
parsingapp()
