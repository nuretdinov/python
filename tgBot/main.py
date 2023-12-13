# aiogram v.2.32
from aiogram import Bot, Dispatcher, executor, types
import requests, json
# токены телеграм и яндекс.погоды
import tg_token, ya_token

TG_TOKEN = tg_token.TG_TOKEN

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)

# получаем погоду от яндекса
def get_weather(lat, lon):
    latitude = lat
    longitude = lon
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = requests.get(url_yandex, headers={'X-Yandex-API-Key': ya_token.YA_TOKEN}, verify=False)
    yandex_json = json.loads(yandex_req.text)
    wind = {"nw":"северо-западный", "n":"северный", "ne":"северо-восточный", "e":"восточный", "se":"юго-восточный", "s":"южный", "sw":"юго-западный", "w":"западный", "c":"штиль"}
    weather = 'Температура: ' + str(yandex_json['fact']['temp']) + "\nВетер: " + str(
        yandex_json['fact']['wind_speed']) + ' м/с ' + str(wind[yandex_json['fact']['wind_dir']])
    return weather

# формируем общее меню с 2мя кнопками
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🌡️ СПб", "🌡️ Мск"]
    keyboard.add(*buttons)
    await message.reply("Привет 🥰 ! Я версия SpeakToMe 1.0\n Сейчас могу показать погоду...", reply_markup=keyboard)

# обработка нажатия на кнопки СПб
@dp.message_handler(lambda message: message.text == "🌡️ СПб")
async def weather_show(message: types.Message):
    weather = get_weather(59.9386, 30.3141)
    await message.reply(weather)

# обработка нажатия на кнопки Мск
@dp.message_handler(lambda message: message.text == "🌡️ Мск")
async def weather_show(message: types.Message):
    weather = get_weather(55.7522, 37.6156)
    await message.reply(weather)

# обработка команды bye
@dp.message_handler(commands=['bye'])
async def send_welcome(message: types.Message):
    await message.reply("До новых встреч\n 🤗🤗🤗 ")

# обработка команды help
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/start - начало работы\n /help - список команд\n /bye - конец работы\n")

# обработка любого текста от пользователя (неизвестного боту)
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Я еще не знаю команду '" + message.text + "'")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)