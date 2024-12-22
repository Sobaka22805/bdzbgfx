from bs4 import BeautifulSoup
import requests
import sqlite3

responce = requests.get('https://sinoptik.ua/')

temperature = []

if responce.status_code == 200:

    item_site = BeautifulSoup(responce.text, features='html.parser')
    weathers = item_site.find_all('div', {'class', 'XyT+Rm+n'})
    days = item_site.find_all('p', {'class', 'BzO81ZRx'})

    for weather in weathers:
        aboba = weather.findNext().text[4:]
        # print('Temperature ->', aboba)
        temperature.append(aboba)

if not len(temperature):
    raise ValueError
# print(temperature)

connection = sqlite3.connect('temperature_db.sl3')
cur_db = connection.cursor()

# cur_db.execute("CREATE TABLE weathers (temperature TEXT);")
# print(temperature[0])

for i in range(len(temperature)):
    # print(temperature[i])
    cur_db.execute("INSERT INTO weathers (temperature) VALUES (?)", (temperature[i],))

cur_db.execute("SELECT temperature FROM weathers;")
result = cur_db.fetchall()
print('Results from DB ->', result)

connection.commit()
connection.close()
