# подключаем библиотеку для работы с запросами
import requests
# указываем город
city = input("Введите город: ")

# формируем запрос
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
"q": city,
"units": "metric",
"lang": "ru",
"appid":"4acf83afc29f617a9e96853116a4aff7"
}

# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url, params=params).json()

# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])

# выводим значения на экран
print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')