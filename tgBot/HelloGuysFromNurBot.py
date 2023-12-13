from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="6625798279:AAHo283Ya5RAQcs_-kXOKgOJLdXhGy26vo8")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["❤️Мурик", "❤️Родька", "❤️Хотян", "❤️Юрка", "❤️Штак"]
    keyboard.add(*buttons)
    await message.reply("Привет мой друг 🥰🥰🥰 Я рад тебя видеть! Кто ты?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "❤️Мурик")
async def weather_show(message: types.Message):
    await message.reply('А ИДИ НА ХУЙ, МУРИК!!!')

@dp.message_handler(lambda message: message.text == "❤️Родька")
async def weather_show(message: types.Message):
    await message.reply('А ИДИ НА ХУЙ, РОДЬКА!!!')

@dp.message_handler(lambda message: message.text == "❤️Хотян")
async def weather_show(message: types.Message):
    await message.reply('А ИДИ НА ХУЙ, ХОТЯН!!!')

@dp.message_handler(lambda message: message.text == "❤️Юрка")
async def weather_show(message: types.Message):
    await message.reply('А ИДИ НА ХУЙ, ЮРКА!!!')

@dp.message_handler(lambda message: message.text == "❤️Штак")
async def weather_show(message: types.Message):
    await message.reply('А ИДИ НА ХУЙ, ШТАК!!!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Сказал же! ИДИ НА ХУЙ!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)