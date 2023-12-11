from aiogram import Bot, Dispatcher, executor, types
import requests, json
import tg_token, ya_token

TG_TOKEN = tg_token.TG_TOKEN

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🌡️ погода", "/bye"]
    keyboard.add(*buttons)
    await message.reply("Привет 🥰 ! Я версия SpeakToMe 1.0\n", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "🌡️ погода")
async def weather_show(message: types.Message):
    latitude = '59.9386'
    longitude = '30.3141'
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = requests.get(url_yandex, headers={'X-Yandex-API-Key': ya_token.YA_TOKEN}, verify=False)
    yandex_json = json.loads(yandex_req.text)
    weather_out = 'Температура: ' + str(yandex_json['fact']['temp']) + "\nВетер: " + str(
        yandex_json['fact']['wind_speed']) + ' м/с'
    await message.reply(weather_out)

@dp.message_handler(commands=['bye'])
async def send_welcome(message: types.Message):
    await message.reply("До новых встреч\n 🤗🤗🤗 ")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Я еще не знаю команду '" + message.text + "'")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)