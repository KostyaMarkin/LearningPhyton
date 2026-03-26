# подключаем библиотеку для работы с запросами
import requests

def wind_direction(deg):
    if deg is None:
        return "неизвестно"
    directions = [
        "северный", "северо-восточный", "восточный", "юго-восточный",
        "южный", "юго-западный", "западный", "северо-западный"
    ]
    idx = round(deg / 45) % 8
    return directions[idx]

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

temperature = round(weather_data['main']['temp'])
feels_like = round(weather_data['main']['feels_like'])
pressure_hpa = weather_data['main']['pressure']
pressure_mm = round(pressure_hpa * 0.75006)  # перевод в мм рт. ст.
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
wind_deg = weather_data['wind'].get('deg')  # может отсутствовать
wind_dir = wind_direction(wind_deg) if wind_deg is not None else "неизвестно"
weather_desc = weather_data['weather'][0]['description']
visibility_km = weather_data.get('visibility', 0) / 1000  # в км, если есть
clouds = weather_data.get('clouds', {}).get('all', 0)  # облачность в %

# Выводим информацию
print("\n=== Погода в городе", city, "===")
print(f"Температура: {temperature} °C")
print(f"Ощущается как: {feels_like} °C")
print(f"Ветер: {wind_speed} м/с, {wind_dir}")
print(f"Давление: {pressure_hpa} гПа ({pressure_mm} мм рт. ст.)")
print(f"Влажность: {humidity} %")
print(f"Облачность: {clouds} %")
print(f"Погодные условия: {weather_desc.capitalize()}")
if visibility_km > 0:
    print(f"Видимость: {visibility_km:.1f} км")