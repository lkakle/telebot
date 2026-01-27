from aiogram import Router, F
from aiogram.types import Message
import requests
import datetime
import math

router = Router()

code_to_smile = {
     "Clear": "Ясно \U00002600",
     "Clouds": "Облачно \U00002601",
     "Rain": "Дождь \U00002614",
     "Drizzle": "Дождь \U00002614",
     "Thunderstorm": "Гроза \U000026A1",
     "Snow": "Снег \U0001F328",
     "Mist": "Туман \U0001F32B"
}

@router.message(F.text.lower().split()[0] == 'погода')
async def message_hundler(message: Message):
    country = message.text.lower().split()
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={country[1]}&lang=ru&units=metric&APPID=1da32ea2a1a3f1f1fdaa1f205f6f71d6", timeout=10)
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        day_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            weather_emoji = code_to_smile[weather_description]
        else:
            weather_emoji = "Бля, чё там, я хуй знает......."

        if datetime.datetime.now().hour <=  datetime.datetime(2024, 1, 2, 5, 0).hour or datetime.datetime.now().hour >= datetime.datetime(2024, 1, 2, 22, 0).hour:
            time_emoji = "Ночь 🌃 "
        elif datetime.datetime.now().hour >=  datetime.datetime(2024, 1, 2, 6, 0).hour and datetime.datetime.now().hour <= datetime.datetime(2024, 1, 2, 11, 0).hour:
            time_emoji = "Утро 🌇 "
        elif datetime.datetime.now().hour >=  datetime.datetime(2024, 1, 2, 12, 0).hour and datetime.datetime.now().hour <= datetime.datetime(2024, 1, 2, 16, 0).hour:
            time_emoji = "День 🏙 "
        else:
            time_emoji = "Вечер 🌆 " 
                
        await message.answer(f"{time_emoji}\n"
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}⌚\n"
                f"Погода в городе: {city}🏙\nТемпература: {cur_temp}°C🌡\n"
                f"{weather_emoji}\n"
                f"Влажность: {humidity}%💧\nДавление: {math.ceil(pressure/1.333)} мм.рт.ст🌡\nВетер: {wind} м/с 🪁\n"
                f"Восход солнца: {sunrise_timestamp.time()}☀\nЗакат солнца: {sunset_timestamp.time()}☀\nПродолжительность дня: {day_time}📅\n"
                f"Хорошего дня!🍀")

    except:
        await message.answer("Второе слово должно быть названием города!")
    