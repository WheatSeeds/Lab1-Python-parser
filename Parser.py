from bs4 import BeautifulSoup
import requests

dict = {'Title': [],
        'Author': [],
        'Price': [],
        }

#Функция записи 3 элементов в словарь, pageLast - количество страниц которые нужно спарсить
def parse(pageLast):
    url = 'https://www.chitai-gorod.ru/search?phrase=python'
    for i in range(1, pageLast + 1):
        page = requests.get(url + '&page=' + str(i))
        soup = BeautifulSoup(page.text, "html.parser")

        block = soup.findAll('article', class_='product-card product-card product')

        for data in block:

            dict['Title'].append(data.find('div', class_='product-title__head').text.strip())

            dict['Author'].append(data.find('div', class_='product-title__author').text.strip())

            if data.find('div', class_='product-price__value'):
                dict['Price'].append(data.find('div', class_='product-price__value').text.strip())
            else:
                dict['Price'].append('Нет в наличии')
