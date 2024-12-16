from bs4 import BeautifulSoup
import requests
import sqlite3

responce = requests.get('https://sinoptik.ua/')

if responce.status_code == 200:

    item_site = BeautifulSoup(responce.text, features='html.parser')
    weathers = item_site.find_all('div', {'class', 'XyT+Rm+n'})
    days = item_site.find_all('p', {'class', 'BzO81ZRx'})

    # Каждая строка, это день, то-есть, 1-я строка = Понедельник, 2-я строка = Вторник и т.д. я не смог реализовать это, извините.
    for weather in weathers:
        aboba = weather.findNext().text[4:].replace('°', '')
        result = float(aboba)
        print(result)

connection = sqlite3.connect('BD.sl3', 10)
cur_db = connection.cursor()

# cur_db.execute("CREATE TABLE weathers (aboba FLOAT);")

cur_db.execute("INSERT INTO weathers (aboba) VALUES (@result);", {'aboba': result})
connection.commit()
connection.close()
