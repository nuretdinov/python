# aiogram v.3.2
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from openai import OpenAI
import logging
import asyncio
import tg_bot_token
from aiogram import F
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

client = OpenAI()


def ask_chatgpt(question):
    question = question
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])
    return completion.choices[0].message.content


TG_TOKEN = tg_bot_token.TG_TOKEN
bot = Bot(token=TG_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello! <b>{message.from_user.full_name}</b>\nЗадавай задачу chatGPT!")


@dp.message(Command("about"))
async def cmd_answer(message: types.Message):
    await message.answer("Бот работает с chatGPT")


@dp.message(F.text)
async def echo(message: Message):
    answer = ask_chatgpt(message.text)
    await message.answer(f"{answer}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
